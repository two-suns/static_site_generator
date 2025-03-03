class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        if children is None:
            self.children = []
        else:
            self.children = children
        
        if props is None:
            self.props = {}
        else:
            self.props = props
            
        self.tag = tag
        self.value = value
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        props_list = []
        for key, value in self.props.items():
            props_list.append(f'{key}="{value}"')
        return " " + " ".join(props_list)
    
    def __repr__(self):
        return (f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag, value, children=None, props=props)
        
    def to_html(self):
        if self.tag is None:
            return self.value
        else:
            props_str = self.props_to_html()
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode tag attribute must have a value.")
        if not self.children:
            raise ValueError("ParentNode children attribute must have a value.")
        
        props_str = self.props_to_html()
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
            