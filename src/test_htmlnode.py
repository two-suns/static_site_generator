import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_empty(self):
        node = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(node.props_to_html(), "")
        
    def test_with_props(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        
    def test_props_with_children(self):
        child_node = HTMLNode(tag="span", value="child text")
        node = HTMLNode(tag="div", children=[child_node])
        self.assertEqual(node.props_to_html(), "")
        
    def test_repr(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com"})
        expected_repr = "HTMLNode(tag='a', value=None, children=[], props={'href': 'https://www.google.com'})"
        self.assertEqual(repr(node), expected_repr)