import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("Here is some text", TextType.ITALIC_TEXT)
        node2 = TextNode("Here is some text", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
        
    def test_equrl(self):
        node = TextNode("This is a url test", TextType.ITALIC_TEXT, "testsite.com")
        node2 = TextNode("This is a url test", TextType.ITALIC_TEXT, "testsite.com")
        self.assertEqual(node, node2)

    def test_urlnone(self):
        node = TextNode("This is a test", TextType.BOLD_TEXT)
        node2 = TextNode("This is a test", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
        
    def test_diffurl(self):
        node = TextNode("Testing", TextType.ITALIC_TEXT, "test.com")
        node2 = TextNode("Testing", TextType.ITALIC_TEXT, "thisisatest.com")
        self.assertNotEqual(node, node2)
        
    def test_onenone(self):
        node = TextNode("Test text", TextType.BOLD_TEXT, "testtext.com")
        node2 = TextNode("Test text", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()