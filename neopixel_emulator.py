import pyglet


class NeoPixel_Emulator(pyglet.window.Window):
    def __init__(self, window_w=1765, window_h=400, pixsize=35):
        super(NeoPixel_Emulator, self).__init__(width=window_w, height=window_h)
        self.batch = pyglet.graphics.Batch()
        self.sprites = []
        self.color_sprites = []
        self.led_group = pyglet.graphics.Group(order=0)
        self.color_group = pyglet.graphics.Group(order=1)
        self.alive = 1
        self.circle_img = pyglet.image.load(f"circle{pixsize}.png")
        self.pixsize = pixsize
        self.n_per_row = window_w // (pixsize)

    def draw_LEDs(self, led_number):
        for led in range(led_number):
            self.color_sprites.append(
                pyglet.sprite.Sprite(
                    img=self.circle_img,
                    batch=self.batch,
                    x=(led - self.n_per_row * (led // self.n_per_row)) * (self.pixsize),
                    y=self.height
                    - (self.pixsize - 1)
                    - ((led // self.n_per_row) * (self.pixsize - 1))
                    - 5,
                    group=self.color_group,
                )
            )
            self.color_sprites[led].color = (0, 0, 0)

    def draw_LED_matrix(self, width, height):
        for y in range(height):
            for x in range(width):
                self.color_sprites.append(
                    pyglet.sprite.Sprite(
                        img=self.circle_img,
                        batch=self.batch,
                        x=x * self.pixsize,
                        y=self.height
                        - (self.pixsize - 1)
                        - (y * (self.pixsize - 1))
                        - 5,
                        group=self.color_group,
                    )
                )
                self.color_sprites[y * width + x].color = (0, 0, 0)

    def map(self, input_val, in_min, in_max, out_min, out_max):
        output = (input_val - in_min) / (in_max - in_min) * (
            out_max - out_min
        ) + out_min
        return output

    def draw_color(self, led_position, color):
        self.color_sprites[led_position].color = color

    def draw_matrix_color(self, x, y, color, width):
        self.color_sprites[y * width + x].color = color

    def change_brightness(self, brightness):
        for sprite in self.color_sprites:
            sprite.opacity = int(self.map(brightness, 0, 100, 0, 255))

    def on_draw(self):
        self.render()

    def render(self):
        self.clear()
        self.batch.draw()
        _ = self.dispatch_events()
        self.flip()
