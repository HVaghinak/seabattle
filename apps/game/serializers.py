import random
from rest_framework import serializers

from apps.game.models import Game
from django.conf import settings


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'

    def create(self, validated_data):
        self.board = []
        self.__generate_board()
        self.__fill_board()
        validated_data['board'] = self.board

        return super().create(validated_data)

    def __generate_board(self):

        for i in range(10):
            board_row = []
            for j in range(10):
                board_row.append(0)
            self.board.append(board_row)

    def __fill_board(self):

        for ship in settings.SHIP_SAMPLES.keys():
            valid = False
            while not valid:

                horizontal_cord = random.randint(1, 10) - 1
                vertical_cord = random.randint(1, 10) - 1
                placement_type = "horizontal" if random.randint(0, 1) else "vertical"

                valid = self.__is_possible_to_place_ship(settings.SHIP_SAMPLES[ship], horizontal_cord, vertical_cord, placement_type)

            self.__place_ship(settings.SHIP_SAMPLES[ship], horizontal_cord, vertical_cord, placement_type)

    def __is_possible_to_place_ship(self, ship_length, horizontal_cord, vertical_cord, placement_type):

        if placement_type == "vertical" and horizontal_cord + ship_length > 10:
            return False
        elif placement_type == "horizontal" and vertical_cord + ship_length > 10:
            return False
        else:
            if placement_type == "vertical":
                for i in range(ship_length):
                    if self.board[horizontal_cord + i][vertical_cord] != 0:
                        return False
            elif placement_type == "horizontal":
                for i in range(ship_length):
                    if self.board[horizontal_cord][vertical_cord + i] != 0:
                        return False

        return True

    def __place_ship(self, ship_length, horizontal_cord, vertical_cord, placement_type):

        if placement_type == "vertical":
            for i in range(ship_length):
                self.board[horizontal_cord + i][vertical_cord] = 1
        elif placement_type == "horizontal":
            for i in range(ship_length):
                self.board[horizontal_cord][vertical_cord + i] = 1
