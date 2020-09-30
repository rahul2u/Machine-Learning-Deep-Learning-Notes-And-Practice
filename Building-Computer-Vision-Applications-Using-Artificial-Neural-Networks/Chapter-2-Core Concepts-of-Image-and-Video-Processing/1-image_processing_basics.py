"""
Image Processing
Image processing is the technique of manipulating a digital image to either get an
enhanced image or extract some useful information from it. In image processing, the
input is an image, and the output may be an image or some characteristics or features
associated with that image. A video is a series of images or frames. Therefore, the
technique of image processing also applies to video processing. In this chapter, I will
explain the core concepts of digital image processing. I will also show you how to work
with images and write code to manipulate them.

============================================================

Image Basics
A digital image is an electronic representation of an object/scene or scanned document.
The digitalization of an image means converting it into a series of numbers and storing
these numbers in a computer storage system. Understanding how these numbers are
arranged and how to manipulate them is the primary objective of this chapter. In this
chapter, I will explain what makes an image and how to manipulate it using OpenCV and
Python.

==================================================

Pixels
Imagine a series of dots arranged in rows and columns, and these dots have different
colors. This is pretty much how an image is formed. The dots that form an image are
called pixels. These pixels are represented by numbers, and the values of the numbers
determine the color of a pixel. Think of an image as a grid of square cells with each cell
consisting of one pixel of a particular color. For example, a 300×400-pixel image means
that the image is organized into a grid of 300 rows and 400 columns. That means our
image has 300×400 = 120,000 pixels.

==============================================

Pixel Color
A pixel is represented in two ways: grayscale and color.
=======================================
Grayscale
In a grayscale image, each pixel takes a value between 0 and 255. The value 0 represents
black, and 255 represents white. The values in between are varying shades of gray. The
values close to 0 are darker shades of gray, and values closer to 255 are brighter shades of
gray.
==================================================
Color
The RGB (which stands for Red, Blue, and Green) color model is one of the most popular
color representations of a pixel. There are other color models, but we will stick to RGB in
this book.

In the RGB model, each pixel is represented as a tuple of three values, generally
represented as follows: (value for red component, value for green component, value for
blue component). Each of the three colors is represented by integers ranging from 0 to
255. Here are some examples:
(0,0,0) is a black color.
(255,0,0) is a pure red color.
(0,255,0) is a pure green color.
What color is represented by (0,0,255)?
What color is represented by (255,255,255)?
This w3school website (https://www.w3schools.com/colors/colors_rgb.asp) is a
great place to play with different combinations of RGB tuples to explore more patterns.
Explore what color is represented by each of the following tuples:
(0,0,128)
(128,0,128)
(128,128,0)
Let’s try to make yellow. Here is a clue: red and green make yellow. That means a
pure red (255), a pure green (255), and no blue (0) will make yellow. So, our RGB tuple
for yellow is (255,255,0).
Now that we have a good understanding of pixels and their color, let’s understand
how pixels are arranged in an image and how to access them. The following section will
discuss the concept of coordinate systems in image processing.




"""