# Created by JaegerwaldDev under the MIT License
# Copyright (c) JaegerwaldDev 2023

from os import system
from random import choice
custom_text=input("Animation Text: ")
hex_colors="0123456789ABCDEF"

def get_rand_color():
    first=choice(hex_colors)
    second=choice(hex_colors)
    while second==first:
        second=choice(hex_colors)
    return(first+second)

system("cls")
system("color 04")
print("EPILEPSY WARNING - IF YOU HAVE PHOTOSENSITIVE EPILEPSY TURN OFF THIS PROGRAM IMMEDIETLY!!!\n")
system("pause")

anim=""".
 .
  .
   .
     .
       .
         .
            .
               .
                  .
                     .
                        .
                           .
                              .
                                 .
                                    .
                                       .
                                         .
                                           .
                                             .
                                              .
                                               .
                                                .
                                                 .
                                                 .
                                                 .
                                                .
                                               .
                                              .
                                             .
                                           .
                                         .
                                       .
                                    .
                                 .
                              .
                           .
                        .
                     .
                  .
               .
            .
         .
       .
     .
   .
  .
 .
.
."""

print(anim.replace(".", custom_text))
while True:
    for line in anim.split("\n"):
        print(line.replace(".", custom_text))
        system("color "+get_rand_color())
