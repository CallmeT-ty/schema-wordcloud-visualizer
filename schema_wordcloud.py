#!/usr/bin/env python3
"""
Schema Word Cloud Visualizer
Generates word clouds from schema types where size represents nesting level
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
import random

def create_mock_invoice_schema():
    """
    Create a mock invoice schema with different nesting levels
    Returns dict with type names and their weights (based on nesting depth)
    """
    schema_hierarchy = {
        # Root level (weight 10) - Main business objects
        "Invoice": 10,
        "Customer": 10,
        
        # Level 1 (weight 8) - Direct children of root
        "LineItem": 8,
        "Payment": 8,
        "Address": 8,
        "Contact": 8,
        
        # Level 2 (weight 6) - Nested objects
        "Product": 6,
        "TaxInfo": 6,
        "ShippingDetails": 6,
        
        # Level 3 (weight 4) - Deeply nested
        "Money": 4,
        "Quantity": 4,
        "Dimensions": 4,
        
        # Level 4 (weight 2) - Leaf types/primitives
        "Currency": 2,
        "Unit": 2,
        "Timestamp": 2,
    }
    
    return schema_hierarchy

def create_circular_mask(size=400):
    """Create a circular mask for the word cloud"""
    mask = np.zeros((size, size), dtype=np.uint8)
    y, x = np.ogrid[:size, :size]
    center = size // 2
    circle_mask = (x - center) ** 2 + (y - center) ** 2 <= (center - 20) ** 2
    mask[circle_mask] = 255
    return mask

def color_func_by_weight(word, font_size, position, orientation, random_state=None, **kwargs):
    """Color function that assigns colors based on font size (which reflects weight)"""
    if font_size > 80:  # Root types
        return f"hsl(220, 80%, 40%)"  # Deep blue
    elif font_size > 60:  # Level 1
        return f"hsl(260, 70%, 50%)"  # Purple
    elif font_size > 40:  # Level 2
        return f"hsl(300, 60%, 60%)"  # Magenta
    elif font_size > 20:  # Level 3
        return f"hsl(340, 50%, 70%)"  # Pink
    else:  # Leaf types
        return f"hsl(20, 40%, 80%)"   # Light orange

def generate_schema_wordcloud(schema_types, title="Schema Types Word Cloud", use_mask=True):
    """
    Generate a word cloud from schema types
    
    Args:
        schema_types: Dict with type names as keys and weights as values
        title: Title for the plot
        use_mask: Whether to use circular mask
    """
    
    # Create mask if requested
    mask = create_circular_mask(400) if use_mask else None
    
    # Create WordCloud object
    wordcloud = WordCloud(
        width=800,
        height=600,
        background_color='white',
        max_words=200,
        relative_scaling=0.5,
        colormap=None,  # We'll use custom color function
        mask=mask,
        collocations=False,  # Avoid combining words
        prefer_horizontal=0.7,  # Prefer horizontal text
        min_font_size=12,
        max_font_size=120
    )
    
    # Generate word cloud from frequencies
    wordcloud.generate_from_frequencies(schema_types)
    
    # Apply custom coloring
    wordcloud.recolor(color_func=color_func_by_weight)
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    
    # Add legend
    legend_elements = [
        plt.Rectangle((0,0),1,1, facecolor='#2C5AA0', label='Root Types (Level 0)'),
        plt.Rectangle((0,0),1,1, facecolor='#6B46C1', label='Level 1'),
        plt.Rectangle((0,0),1,1, facecolor='#C026D3', label='Level 2'),
        plt.Rectangle((0,0),1,1, facecolor='#E11D48', label='Level 3'),
        plt.Rectangle((0,0),1,1, facecolor='#EA580C', label='Leaf Types (Level 4+)')
    ]
    plt.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.1, 1))
    
    plt.tight_layout()
    return wordcloud

def print_schema_info(schema_types):
    """Print information about the schema hierarchy"""
    print("Schema Type Hierarchy:")
    print("=" * 40)
    
    # Group by weight (nesting level)
    levels = {}
    for type_name, weight in schema_types.items():
        if weight not in levels:
            levels[weight] = []
        levels[weight].append(type_name)
    
    # Print by level
    level_names = {10: "Root", 8: "Level 1", 6: "Level 2", 4: "Level 3", 2: "Leaf"}
    for weight in sorted(levels.keys(), reverse=True):
        level_name = level_names.get(weight, f"Level (weight {weight})")
        types = ", ".join(sorted(levels[weight]))
        print(f"{level_name:10}: {types}")
    print()

def main():
    """Main function to demonstrate schema word cloud generation"""
    print("Schema Word Cloud Visualizer")
    print("=" * 40)
    
    # Create mock schema
    schema_types = create_mock_invoice_schema()
    
    # Print schema information
    print_schema_info(schema_types)
    
    # Generate word clouds with different styles
    
    # Style 1: Circular mask
    print("Generating circular word cloud...")
    wordcloud1 = generate_schema_wordcloud(
        schema_types, 
        "Invoice Schema - Circular Layout", 
        use_mask=True
    )
    plt.savefig('schema_wordcloud_circular.png', dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory
    
    # Style 2: Rectangular layout
    print("Generating rectangular word cloud...")
    wordcloud2 = generate_schema_wordcloud(
        schema_types, 
        "Invoice Schema - Rectangular Layout", 
        use_mask=False
    )
    plt.savefig('schema_wordcloud_rectangular.png', dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory
    
    print("Word clouds saved as 'schema_wordcloud_circular.png' and 'schema_wordcloud_rectangular.png'")

if __name__ == "__main__":
    main() 