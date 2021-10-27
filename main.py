"""
TP2 - Dessiner avec Arcade
Par: Qian Qian
Groupe: 407

Ce programme dessine une image inspirée par l'image du Collège de Montréal
"""

# Importer la librairie Arcade
import arcade


def draw_windows_ltr(left, bottom, height, width, space, windows_number):
    """
    C'est une fonction qui dessine des fenêtres de même hauteur et largeur à partir de deux côtés
    (de gauche à droite)
    :param left: Le côté gauche à commencer
    :param bottom: Le côté bas à commencer
    :param height: La hauteur des fenêtres
    :param width: La largeur des fenêtres
    :param space: L'espace entre les fenêtres
    :param windows_number: Nombre des fênetres
    :return: None
    """

    for i in range(windows_number):
        # Dessiner une fenêtre
        arcade.draw_lrtb_rectangle_filled(left, left + width, bottom + height, bottom, arcade.color.LIGHT_SKY_BLUE)
        # Trouver la coordination de prochaine fenêtre
        left += width + space
        # Boucle jusqu'à la dernière fenêtre


def draw_windows_rtl(right, bottom, height, width, space, windows_number):
    """
    C'est une fonction qui dessine des fenêtres de même hauteur et largeur à partir de deux côtés
    (de droite à gauche)
    :param right: Le côté droite à commencer
    :param bottom: Le côté bas à commencer
    :param height: La hauteur des fenêtres
    :param width: La largeur des fenêtres
    :param space: L'espace entre les fenêtres
    :param windows_number: Nombre des fênetres
    :return: None
    """

    for i in range(windows_number):
        # Dessiner une fenêtre
        arcade.draw_lrtb_rectangle_filled(right - width, right, bottom + height, bottom, arcade.color.LIGHT_SKY_BLUE)
        # Trouver la coordination de prochaine fenêtre
        right -= width + space
        # Boucle jusqu'à la dernière fenêtre


# Les constants
# La hauteur en pixel de la fenêtre
SCREEN_HEIGHT = 720
# La largeur en pixel de la fenêtre
SCREEN_WIDTH = 1024
# Le titre de la fenêtre
TITLE = "Qian Qian - TP2 - Dessiner avec Arcade"

# Les positions relatives
# 1/2 d'hauteur
HEIGHT_HALF = SCREEN_HEIGHT / 2
# 1/3 d'hauteur
HEIGHT_FIRST_THIRD = SCREEN_HEIGHT / 3
# 2/3 d'hauteur
HEIGHT_SECOND_THIRD = SCREEN_HEIGHT / 3 * 2
# 1/2 de largueur
WIDTH_HALF = SCREEN_WIDTH / 2
# 1/3 de largueur
WIDTH_FIRST_THIRD = SCREEN_WIDTH / 3
# 2/3 de largueur
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
    # Dessiner les fênetres à gauche de première étage
    draw_windows_ltr(SCREEN_WIDTH / 36, SCREEN_HEIGHT / 24,
                     HEIGHT_SECOND_THIRD / 4, SCREEN_WIDTH / 15,
                     SCREEN_WIDTH / 32, 3)
    # Dessiner les fênetres à droite de première étage
    draw_windows_rtl(SCREEN_WIDTH / 36 * 35, SCREEN_HEIGHT / 24,
                     HEIGHT_SECOND_THIRD / 4, SCREEN_WIDTH / 15,
                     SCREEN_WIDTH / 32, 3)
    # Fenêtres de deuxième étage
    draw_windows_ltr(SCREEN_WIDTH / 36, SCREEN_HEIGHT / 3,
                     HEIGHT_SECOND_THIRD / 4, SCREEN_WIDTH / 15,
                     SCREEN_WIDTH / 32, 3)
    draw_windows_rtl(SCREEN_WIDTH / 36 * 35, SCREEN_HEIGHT / 3,
                     HEIGHT_SECOND_THIRD / 4, SCREEN_WIDTH / 15,
                     SCREEN_WIDTH / 32, 3)
    # Dessiner la porte
    arcade.draw_lrtb_rectangle_filled(WIDTH_HALF - SCREEN_WIDTH / 24, WIDTH_HALF + SCREEN_WIDTH / 24,
                                      HEIGHT_SECOND_THIRD / 3, HEIGHT_SECOND_THIRD / 24,
                                      (111, 67, 42))
    arcade.draw_line(WIDTH_HALF - SCREEN_WIDTH / 6, 0,
                     WIDTH_HALF - SCREEN_WIDTH / 6, HEIGHT_SECOND_THIRD,
                     arcade.color.BEIGE, 15)
    arcade.draw_line(WIDTH_HALF + SCREEN_WIDTH / 6, 0,
                     WIDTH_HALF + SCREEN_WIDTH / 6, HEIGHT_SECOND_THIRD,
                     arcade.color.BEIGE, 15)
    arcade.draw_triangle_filled(WIDTH_HALF, SCREEN_HEIGHT / 24 * 21,
                                WIDTH_HALF - SCREEN_WIDTH / 6, HEIGHT_SECOND_THIRD,
                                WIDTH_HALF + SCREEN_WIDTH / 6, HEIGHT_SECOND_THIRD,
                                (99, 99, 102))
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, HEIGHT_SECOND_THIRD * 1.05, HEIGHT_SECOND_THIRD, (72, 72, 74))
    roof_lines = [(WIDTH_HALF - SCREEN_WIDTH / 6, HEIGHT_SECOND_THIRD * 1.01),
                  (WIDTH_HALF, SCREEN_HEIGHT / 24 * 21),
                  (WIDTH_HALF + SCREEN_WIDTH / 6, HEIGHT_SECOND_THIRD * 1.01)]
    arcade.draw_line_strip(roof_lines, (72, 72, 74), 20)
    # Dessiner la cercle
    arcade.draw_circle_filled(WIDTH_HALF, HEIGHT_SECOND_THIRD * 1.15, 35, arcade.color.LIGHT_SKY_BLUE)
    # Dessiner les arbres
    arcade.draw_rectangle_filled(120, 60, 50, 150, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(120, 210, 150, 200, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(300, 60, 50, 150, arcade.csscolor.SIENNA)
    arcade.draw_arc_filled(300, 120, 150, 250, arcade.csscolor.DARK_GREEN, 0, 180)
    arcade.draw_rectangle_filled(SCREEN_WIDTH - 300, 60, 50, 150, arcade.csscolor.SIENNA)
    arcade.draw_ellipse_filled(SCREEN_WIDTH - 300, 210, 150, 200, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(SCREEN_WIDTH - 120, 60, 50, 150, arcade.csscolor.SIENNA)
    arcade.draw_arc_filled(SCREEN_WIDTH - 120, 120, 150, 250, arcade.csscolor.DARK_GREEN, 0, 180)
    # Dessiner les polygones
    arcade.draw_polygon_filled(((WIDTH_HALF, 400),
                                (WIDTH_HALF - 40, 360),
                                (WIDTH_HALF - 25, 320),
                                (WIDTH_HALF + 25, 320),
                                (WIDTH_HALF + 40, 360)
                                ),
                               arcade.csscolor.LIGHT_SKY_BLUE)
    # Texte
    arcade.draw_text("Collège de Mont Réal", WIDTH_HALF - SCREEN_WIDTH / 16, HEIGHT_FIRST_THIRD - 50, arcade.color.BARBIE_PINK)
    # Finir de dessiner
    arcade.finish_render()
    # Garder la fenêtre ouvert
    arcade.run()


main()
