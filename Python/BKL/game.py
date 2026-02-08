from ursina import *
import random

app = Ursina()

window.title = "Archery Game"
window.color = color.black

# Ground
ground = Entity(
    model='plane',
    scale=(40, 1, 40),
    color=color.green,
    collider='box'
)

# Player / Bow
bow = Entity(
    model='cube',
    color=color.orange,
    scale=(0.5, 2, 0.5),
    position=(0, 1, -15)
)

camera.parent = bow
camera.position = (0, 5, -10)
camera.rotation_x = 10

# Target
target = Entity(
    model='cube',
    color=color.red,
    scale=(2, 2, 0.5),
    position=(random.randint(-10, 10), 1, 15),
    collider='box'
)

score = 0
score_text = Text(text="Score: 0", position=(-0.85, 0.45), scale=2)

arrow = None
power = 0
charging = False

def input(key):
    global charging, power, arrow

    if key == 'left mouse down':
        charging = True
        power = 0

    if key == 'left mouse up' and charging:
        charging = False
        shoot_arrow()

def shoot_arrow():
    global arrow, power

    arrow = Entity(
        model='cube',
        color=color.white,
        scale=(0.2, 0.2, 2),
        position=bow.position + bow.forward * 2,
        rotation=bow.rotation,
        collider='box'
    )
    arrow.speed = min(power * 2, 25)

def update():
    global power, score

    # Aim with mouse
    bow.rotation_y += mouse.velocity[0] * 40

    # Charging power
    if charging:
        power += time.dt * 10

    # Arrow movement
    if arrow:
        arrow.position += arrow.forward * arrow.speed * time.dt

        if arrow.intersects(target).hit:
            score += 10
            score_text.text = f"Score: {score}"
            arrow.disable()

            target.x = random.randint(-10, 10)
            target.z = random.randint(10, 20)

        if arrow.z > 30:
            arrow.disable()

app.run()
