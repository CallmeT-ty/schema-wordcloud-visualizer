# Schema Word Cloud Visualizer

This project demonstrates how to use Python's `wordcloud` library to visualize schema hierarchies where the size of each type name represents its nesting level in the schema.

## Concept

- **Root types** (e.g., `Invoice`, `Customer`) are rendered largest
- **Direct children** (e.g., `LineItem`, `Payment`) are medium-sized
- **Nested objects** get progressively smaller based on depth
- **Leaf types/primitives** (e.g., `Currency`, `Unit`) are smallest

## Project Structure

```
schema-wordcloud-project/
├── simple_schema_wordcloud.py     # Basic implementation
├── schema_wordcloud.py            # Advanced implementation
├── requirements.txt               # Python dependencies
├── README_Schema_WordCloud.md     # This documentation
├── schema_wordcloud_venv/         # Virtual environment (after setup)
├── simple_schema_wordcloud.png    # Generated: Basic word cloud
├── schema_wordcloud_circular.png  # Generated: Circular layout
└── schema_wordcloud_rectangular.png # Generated: Rectangular layout
```

## Files

### `simple_schema_wordcloud.py`
- Basic implementation with minimal features
- Generates a simple word cloud with size-based hierarchy
- Good starting point for understanding the concept

### `schema_wordcloud.py` 
- Advanced implementation with enhanced features:
  - **Color coding**: Different colors for each nesting level
  - **Multiple layouts**: Circular and rectangular masks
  - **Legend**: Shows which colors represent which levels
  - **Better customization**: Font sizes, spacing, etc.

### `requirements.txt`
- Lists all Python dependencies needed

## Usage

1. **Navigate to project folder:**
   ```bash
   cd schema-wordcloud-project
   ```

2. **Install dependencies:**
   ```bash
   python3 -m venv schema_wordcloud_venv
   source schema_wordcloud_venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run simple version:**
   ```bash
   python simple_schema_wordcloud.py
   ```

4. **Run advanced version:**
   ```bash
   python schema_wordcloud.py
   ```

## Output

The scripts generate PNG files:
- `simple_schema_wordcloud.png` - Basic word cloud
- `schema_wordcloud_circular.png` - Advanced circular layout
- `schema_wordcloud_rectangular.png` - Advanced rectangular layout

## Example Schema Hierarchy

```
Root Level (Weight 10):     Invoice, Customer
Level 1    (Weight 8):      LineItem, Payment, Address, Contact  
Level 2    (Weight 6):      Product, TaxInfo, ShippingDetails
Level 3    (Weight 4):      Money, Quantity, Dimensions
Leaf Types (Weight 2):      Currency, Unit, Timestamp
```

## Customization

To use with your own schema:

1. **Replace the schema data** in `create_mock_invoice_schema()`:
   ```python
   schema_hierarchy = {
       "YourRootType": 10,
       "YourChildType": 8,
       "YourNestedType": 6,
       # ... etc
   }
   ```

2. **Adjust weights** based on your schema depth:
   - Root types: 10
   - Level 1: 8  
   - Level 2: 6
   - Level 3: 4
   - Leaf types: 2

3. **Customize colors** in `color_func_by_weight()` function

## Benefits of This Approach

✅ **Visual Hierarchy**: Immediately see which types are most important  
✅ **Schema Overview**: Get a bird's-eye view of your data model  
✅ **Documentation**: Create visual documentation for complex schemas  
✅ **Analysis**: Identify deeply nested or overly complex structures  
✅ **Presentation**: Great for explaining schemas to stakeholders  

## Advanced Features

The advanced version includes:
- HSL color gradients for better visual distinction
- Circular mask for more aesthetic layouts
- Custom legend showing level meanings
- Higher resolution output (300 DPI)
- Memory management (closes figures after saving)

## Possible Extensions

- **TypeScript Integration**: Parse actual `.ts` files to extract types
- **JSON Schema Support**: Parse JSON Schema definitions
- **Interactive Version**: Use D3.js for clickable, zoomable visualizations
- **GraphQL Integration**: Visualize GraphQL schema types
- **Database Schema**: Adapt for SQL table relationships
- **API Documentation**: Generate visual API documentation 