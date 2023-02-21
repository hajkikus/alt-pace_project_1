import random

def first_choice():
  a = input("Input a number: ")
  b = input("Input measure of time: ")
  c = input("Input mode of transportation: ")
  d = input("Input adjective: ")
  e = input("Input adjective again: ")
  f = input("Input noun (plural): ")
  g = input("Input a color: ")
  h = input("Input part of the body: ")
  i = input("Input a verb: ")
  j = input("Input a number again: ")
  k = input("Input a noun again: ")
  l = input("Input a noun again: ")
  m = input("Input part of the body again: ")
  o = input("Input a noun again: ")
  p = input("Input adjective again: ")
  q = input("Input a silly word: ")
  print(f"""  It was about {a} {b} ago when I arrived at the hospital in a {c}. The hospital is a/an {d} place, there are a lot of {e} {f} here. There are nurses here who have {g} {h}. If someone wants to come into my room I told them that they have to {i} first. I’ve decorated my room with {j} {k}. Today I talked to a doctor and they were wearing a {l} on their {m}. I heard that all doctors {i} {o} every day for breakfast. The most {p} thing about being in the hospital is the {q} {f}!""")

def second_choice():
  a = input("Input proper noun (person’s name): ")
  b = input("Input noun: ")
  c = input("Input adjective (feeling): ")
  d = input("Input a verb: ")
  e = input("Input adjective (feeling) again: ")
  f = input("Input an animal: ")
  g = input("Input a verb again: ")
  h = input("Input a color: ")
  i = input("Input a verb + ing: ")
  j = input("Input a adverb + ly: ")
  k = input("Input a number: ")
  l = input("Input measure of time: ")
  p = input("Input a silly word: ")
  q = input("Input a noun again: ")
  print(f"""  This weekend I am going camping with {a}. I packed my lantern, sleeping bag, and {b}. I am so {c} to {d} in a tent. I am {e} we might see a(n) {f}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {g}. I have heard that the {h} lake is great for {i}. Then we will {j} hike throughthe forest for {k} {l}. If I see a {h} {f} while hiking, I am going to bring it home as a pet! At night we will tell {k} {p} stories and roast {q} around the campfire!!""")
def third_choice():
  a = input("Input proper noun (person’s name): ")
  b = input("Input adjective: ")
  c = input("Input a color: ")
  d = input("Input an animal: ")
  e = input("Input place: ")
  f = input("Input adjective again: ")
  g = input("Input magical creature (plural): ")
  h = input("Input adjective again: ")
  i = input("Input magical creature (plural) again: ")
  j = input("Input room in a house: ")
  k = input("Input noun: ")
  l = input("Input a noun again: ")
  m = input("Input a noun (plural) again: ")
  n = input("Input adjective again: ")
  o = input("Input a noun (plural) again: ")
  p = input("Input a number: ")
  q = input("Input measure of time: ")
  r = input("Input verb + ing: ")
  s = input("Input adjective 5: ")
  t = input("Input noun 5: ")
  print(f"""  Dear {a}, I am writing to you from a {b} castle in an enchanted forest. I found myself here one day after going for a ride on a {c} {d} in {e}. There are {f} {g} and {h} {i} here! In the {j} there is a pool full of {k}. I fall asleep each night on a {l} of {m} and dream of {n}  {o}. It feels as though I have lived here for {p} {q}. I hope one day you can visit, although the only way to get here now is {r} on a {s} {t}!!""")

def random_stories():
  story = random.choice([1, 2, 3])
  if story == 1:
      first_choice()
  elif story == 2:
      second_choice()
  elif story == 3:
      third_choice()

while True:
  try:
    story = int(input("Input number of story (1, 2 or 3): "))
    if story in [1, 2, 3]:
      random_stories() 
    else:
      raise Exception
    break
  except:
    print("Please input correct number (1, 2 or 3)")
