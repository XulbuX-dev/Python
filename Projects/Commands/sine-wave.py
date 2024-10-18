from typing import Generator
import math
import time


def smooth_wave(amplitude:int, speed:tuple[float]) -> Generator[any, any, any]:
  while True:
    for i in range(0, 361):
      angle = math.radians(i * speed[0])
      value = amplitude * (math.sin(angle))
      yield value
      time.sleep(1 / (speed[1] * 100))

def show_wave(width:int, speed:tuple[float,int] = (10, 1), chars:list[str] = ['█', ' ']) -> None:
  for i in smooth_wave(amplitude=round(width / 2), speed=speed):
    idx = int(i + (width // 2))
    print(idx * chars[0] + chars[1] + (width - idx) * chars[0])


if __name__ == '__main__':
  try:
    print()
    show_wave(width=40)
  except KeyboardInterrupt:
    print()