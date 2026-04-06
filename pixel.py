"""Basic pixel properties."""


class Pixel:
    """Pixel properties in an LED strip.

    Parameters
    ----------

    position : `int`
       Position in strip for this pixel.
       sets color to (0,0,0)

    """

    def __init__(self, position: int):
        self.position = position
        self.current_color = (0, 0, 0)

    def update_color(self, new_color: tuple[int, int, int]):
        """Change pixel color.

        Args:
            new_color: Color 3-tuple R,G,B.
        """
        self.current_color = new_color

    def get_position(self) -> int:
        """Get position in LED strip of pixel.

        Returns:
            position: int
        """
        return self.position

    def get_color(self) -> tuple[int, int, int]:
        """Get color of this pixel.

        Returns:
            color: 3-tuple R,G,B.
        """
        return self.current_color
