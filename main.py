"""
TP2 - Dessiner avec Arcade
Par: Qian Qian
Groupe: 407
"""

# Importer la librairie Arcade
import arcade


def draw_window(left, top, height, width, windows_number):
    """
    C'est une fonction qui dessine des fenêtres de même hauteur et largeur à partir de deux côtés
    :param left: Le côté gauche à commencer
    :param top: Le côté bas à commencer
    :param height: La hauteur des fenêtres
    :param width: La largeur des fenêtres
    :param windows_number: Nombre des fênetres
    :return: None
    """

    pass


# Les constants
# La hauteur en pixel de la fenêtre
SCREEN_HEIGHT = 720
# La largeur en pixel de la fenêtre
SCREEN_WIDTH = 1024
# Le titre de la fenêtre
TITLE = "Qian Qian - TP2 - Dessiner avec Arcade"

HEIGHT_HALF = SCREEN_HEIGHT / 2
HEIGHT_FIRST_THIRD = SCREEN_HEIGHT / 3
HEIGHT_SECOND_THIRD = SCREEN_HEIGHT / 3 * 2

WIDTH_HALF = SCREEN_WIDTH / 2
WIDTH_FIRST_THIRD = SCREEN_WIDTH / 3
WIDTH_SECOND_THIRD = SCREEN_WIDTH / 3 * 2


def main():
    # Ouvrir la fênetre
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    # Changer la couleur de l'arrière plan
    arcade.set_background_color(arcade.color.DARK_SKY_BLUE)
    # Commencer à dessiner
    arcade.start_render()
    # Dessiner le rectangle
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, HEIGHT_SECOND_THIRD, 0, (99, 99, 102))
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, HEIGHT_SECOND_THIRD * 1.05, HEIGHT_SECOND_THIRD, (72, 72, 74))
    #
    #
    # Finir de dessiner
    arcade.finish_render()
    # Garder la fenêtre ouvert
    arcade.run()
    pass


main()
