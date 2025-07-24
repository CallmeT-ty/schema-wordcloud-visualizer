#!/usr/bin/env python3
"""
Simple Schema Word Cloud Example
Basic demonstration of schema visualization using word clouds
"""

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def main():
    # Mock invoice schema with weights based on nesting level
    schema_types = {
        # Root level (biggest)
        "Invoice": 10,
        "Customer": 10,
        
        # Level 1
        "LineItem": 8,
        "Payment": 8,
        "Address": 8,
        "Contact": 8,
        
        # Level 2
        "Product": 6,
        "TaxInfo": 6,
        "ShippingDetails": 6,
        
        # Level 3
        "Money": 4,
        "Quantity": 4,
        "Dimensions": 4,
        
        # Leaf types (smallest)
        "Currency": 2,
        "Unit": 2,
        "Timestamp": 2,
    }
    
    print("Schema hierarchy by weight:")
    for name, weight in sorted(schema_types.items(), key=lambda x: x[1], reverse=True):
        print(f"{name:15}: {weight}")
    
    # Generate word cloud
    wordcloud = WordCloud(
        width=800, 
        height=400, 
        background_color='white',
        max_font_size=100,
        min_font_size=20
    ).generate_from_frequencies(schema_types)
    
    # Display and save
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Invoice Schema Types - Size by Nesting Level', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('simple_schema_wordcloud.png', dpi=150, bbox_inches='tight')
    
    print("\nWord cloud saved as 'simple_schema_wordcloud.png'")
    print("✅ Successfully generated schema word cloud!")

if __name__ == "__main__":
    main() 