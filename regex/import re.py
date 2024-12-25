import re

# Sample text with HTML content
html_text = """
<div style="background-color: orange;">1</div>
<div style="background-color: orange;">2</div>
<div style="background-color: blue;">3</div>
<div style="background-color: orange;">4</div>
<div style="background-color: orange;">6</div>
<div style="background-color: orange;">7</div>
<div style="background-color: blue;">8</div>
<div style="background-color: orange;">9</div>
<div style="background-color: orange;">10</div>
<div style="background-color: orange;">11</div>
<div style="background-color: blue;">648</div>
<div style="background-color: orange;">650</div>
"""

# Regex pattern to match numbers inside div with orange background
pattern = r'<div\s+style="background-color:\s*orange;">(\d+)</div>'

# Find all matches
numbers = re.findall(pattern, html_text)

# Output the list of numbers
print(numbers)

# import re

# # Sample text
# text = '''
# {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
# '''

# # Regex to find numbers with an orange color background
# # Assuming numbers with orange background are surrounded by <i></i> tags
# regex = r'(?<=<i>)(\d+)(?=</i>)'

# # Example of modifying the input text (italicizing some numbers for demonstration)
# # Let's add <i> tags around numbers 1, 2, and 3 as an example of orange-background numbers
# modified_text = text.replace('"id":1', '"id":<i>1</i>').replace('"id":2', '"id":<i>2</i>').replace('"id":3', '"id":<i>3</i>').replace('"id":4', '"id":<i>4</i>').replace('"id":5', '"id":<i>5</i>').replace('"id":6', '"id":<i>6</i>').replace('"id":7', '"id":<i>7</i>').replace('"id":8', '"id":<i>8</i>').replace('"id":9', '"id":<i>9</i>').replace('"id":10', '"id":<i>10</i>').replace('"id":11', '"id":<i>11</i>').replace('"id":648', '"id":<i>648</i>').replace('"id":649', '"id":<i>649</i>').replace('"id":650', '"id":<i>650</i>').replace('"id":651', '"id":<i>651</i>').replace('"id":652', '"id":<i>652</i>').replace('"id":653', '"id":<i>653</i>')

# # Find all matches
# numbers_with_orange_background = re.findall(regex, modified_text)

# # Output the result
# print(numbers_with_orange_background)
