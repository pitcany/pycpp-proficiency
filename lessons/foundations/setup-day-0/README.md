# Setup (Day 0)

**Language**: Mixed (Python + C++)
**Time Estimate**: 2-4 hours
**Notion Source**: [Link](https://www.notion.so/2dc342cf7cc880439ef1cd8049f3df3d)

## Learning Objectives

By the end of this lesson, you should be able to:

- [ ] Verify working Python 3.10+ environment
- [ ] Verify working C++ compiler (g++ 9+ or clang 12+)
- [ ] Install required packages with version pins
- [ ] Verify sanitizers support

## Sections

### Python Setup

Ensure you have Python 3.10 or later installed. We recommend using `uv` for environment management.

```bash
# Check Python version
python3 --version

# Create virtual environment with uv
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -e ".[dev]"
```

### C++ Setup

Verify your C++ compiler supports C++17 or later (C++20 preferred).

```bash
# Check compiler version
g++ --version   # Should be 9+ for full C++17
clang++ --version  # Should be 12+ for full C++17

# Test compilation
echo 'int main() { return 0; }' | g++ -std=c++17 -x c++ -
```

### Troubleshooting

Common issues and solutions:

1. **Python not found**: Ensure Python is in your PATH
2. **Compiler errors**: Update to a modern compiler version
3. **Sanitizer issues**: Some platforms require additional packages

## Verification

Run the verification script to ensure your environment is correctly configured:

```bash
./scripts/check.sh
```

## Next Steps

Once setup is complete, proceed to [Algorithmic Thinking](../algorithmic-thinking/README.md).
