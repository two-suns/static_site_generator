from textnode import TextType, TextNode

def main():
    instance = TextNode("text", TextType.BOLD_TEXT, "test.com")
    print(instance)

main()