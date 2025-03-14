# You are given an HTML code snippet of  lines.
# Your task is to detect and print all the HTML tags, attributes and attribute values.

# Print the detected items in the following format:

# Tag1
# Tag2
# -> Attribute2[0] > Attribute_value2[0]
# -> Attribute2[1] > Attribute_value2[1]
# -> Attribute2[2] > Attribute_value2[2]
# Tag3
# -> Attribute3[0] > Attribute_value3[0]


# The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
# The > symbol acts as a separator of attributes and attribute values.

# If an HTML tag has no attribute then simply print the name of the tag.

# Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
# All attributes have an attribute value.

# Input Format

# The first line contains an integer , the number of lines in the HTML code snippet.
# The next  lines contain HTML code.

# Constraints


# Output Format

# Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.

# Format your answers as explained in the problem statement.

# Sample Input

# 9
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash" 
#   data="your-file.swf" 
#   width="0" height="0">
#   <!-- <param name="movie" value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>
# Sample Output

# head
# title
# object
# -> type > application/x-flash
# -> data > your-file.swf
# -> width > 0
# -> height > 0
# param
# -> name > quality
# -> value > high
# Explanation

# head tag: Print the head tag only because it has no attribute.

# title tag: Print the title tag only because it has no attribute.

# object tag: Print the object tag. In the next  lines, print the attributes type, data, width and                     height along with their respective values.

# <!-- Comment --> tag: Don't detect anything inside it.

# param tag: Print the param tag. In the next  lines, print the attributes name along with                     their respective values.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_comment = False  # To track comments

    def handle_starttag(self, tag, attrs):
        if not self.in_comment:  # Ignore if inside comment
            print(tag)
            for attr, value in attrs:
                print(f"-> {attr} > {value}")

    def handle_endtag(self, tag):
        pass  # We only care about start tags

    def handle_comment(self, data):
        self.in_comment = True  # Start ignoring content in comment
        pass  # We ignore comments completely

    def handle_data(self, data):
        self.in_comment = False  # Stop ignoring when out of comment
        pass  # No need to process raw text data

# Step 1: Read input
n = int(input())  # Number of lines
html_data = "\n".join(input() for _ in range(n))  # Read all lines into a string

# Step 2: Parse the HTML content
parser = MyHTMLParser()
parser.feed(html_data)

# Time and Space Complexity Analysis for the HTMLParser Approach
# Let's analyze the time and space complexities of the solution.

# Time Complexity Analysis
# Parsing the Input
# Reading N lines of input and concatenating them into a single string:
# O(N)
# Processing HTML using HTMLParser
# feed(html_data) processes the HTML linearly.
# handle_starttag(self, tag, attrs):
# Called once per tag → O(T) (T = number of tags)
# Iterates over attributes → O(A) (A = total number of attributes across all tags)
# handle_comment(self, data):
# Called once per comment → O(C) (C = number of comment blocks)
# handle_data(self, data):
# Called once per data section (text nodes) → O(D) (D = number of data nodes)
# Overall, since parsing is linear in the number of characters, we approximate:

# O(K), where K is the total number of characters in the HTML snippet.
# In practice, K ≈ N (since input consists of N lines, each having a constant number of characters).
# Thus, time complexity is O(N + A) (where A is small compared to N in most cases).

# Space Complexity Analysis
# Input Storage
# We store the HTML snippet as a single string: O(N)
# Parser Memory Usage
# The parser stores:
# The current state of parsing (constant extra memory) O(1)
# No additional data structures for results; prints directly.
# Thus, total space complexity is:

# O(N) (for input storage)
# O(1) (for parser state)
# Final Complexity
# Time Complexity: O(N + A) ≈ O(N)
# Space Complexity: O(N) (dominant factor is input storage)
# Since parsing and processing each character happens once, the approach is efficient.