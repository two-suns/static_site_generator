import unittest

from htmlnode import HTMLNode, LeafNode

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
        
    
class TestLeafNode(unittest.TestCase):
    def test_leaf_node_init(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.tag, "p")
        self.assertEqual(leaf.value, "This is a paragraph of text.")
        self.assertEqual(leaf.children, [])
        self.assertEqual(leaf.props, {})
    
    def test_leaf_node_initialization_with_props(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.tag, "a")
        self.assertEqual(leaf.value, "Click me!")
        self.assertEqual(leaf.children, [])
        self.assertEqual(leaf.props, {"href": "https://www.google.com"})

    def test_leaf_node_to_html(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_node_to_html_with_props(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_node_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_node_no_tag(self):
        leaf = LeafNode(None, "This is raw text.")
        self.assertEqual(leaf.to_html(), "This is raw text.")