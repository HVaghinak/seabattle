from django.conf import settings

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.serializers import ValidationError
from rest_framework import status
from rest_framework.response import Response


from apps.game.models import Game
from apps.game.serializers import GameSerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    http_method_names = ['get', 'post']


class ShotAPIView(APIView):

    def post(self, request):

        horizontal_cord, vertical_cord, game = self.validate(request)
        ships_total_length = sum(settings.SHIP_SAMPLES.values())
        response_text = 'You missed :('
        if game.board[horizontal_cord][vertical_cord] == 1:
            game.board[horizontal_cord][vertical_cord] = '*'
            game.max_hit_ships += 1
            response_text = 'You hit the ship'
            if game.max_hit_ships == ships_total_length:
                response_text = 'All ships are destroyed'
                game.is_finished = True
            game.save()
        elif game.board[horizontal_cord][vertical_cord] == '*':
            response_text = 'You already hit with this cords'

        return Response(response_text, status=status.HTTP_200_OK)

    def validate(self, request):

        if not any(
                [request.data.get('horizontal_cord'), request.data.get('vertical_cord'), request.data.get('game_id')]):
            raise ValidationError('You must provide cords and game id')

        try:
            horizontal_cord, vertical_cord, game_id = (
                int(request.data['horizontal_cord']),
                int(request.data['vertical_cord']),
                int(request.data['game_id'])
            )
        except ValueError:
            raise ValidationError('Cords and game id must be integers')

        try:
            game = Game.objects.get(id=request.data['game_id'])
        except Game.DoesNotExist:
            raise ValidationError('You need to create game and after provide game id')
        else:
            if game.is_finished:
                raise ValidationError('This game is finished please start new one')

        if not (0 < horizontal_cord < 11) or not(0 < vertical_cord < 11):
            raise ValidationError('Cords must be in range from 1 to 10')

        return horizontal_cord - 1, vertical_cord - 1, game
