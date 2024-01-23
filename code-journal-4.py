class Animal:
  def __init__(Cats, animal, arms, legs, eyes, tail, furry):
    Cats.animal = animal
    Cats.arms = arms
    Cats.legs = legs
    Cats.eyes = eyes
    Cats.tail = tail
    Cats.furry = furry

  def __str__(Cats):
    return f"My favorite animal is a {Cats.animal}. Cats arms are {Cats.arms} inches long and their legs are {Cats.legs} inches long. Cats have {Cats.eyes} eyes and the fact that they have a tail is {Cats.tail}. The fact that they are furry is also, in most cases, {Cats.furry}."

c1 = Animal("cat", 2.0, 3.0, 2, "True", "True")

print(c1)

 




