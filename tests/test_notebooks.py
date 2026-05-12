"""
Tests for Jupyter notebooks to ensure they execute without errors.
"""

import pytest
import os
import sys
from pathlib import Path
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError


class TestNotebooks:
    """Test execution of Jupyter notebooks."""
    
    @pytest.fixture
    def notebook_paths(self):
        """Get paths to all Python agent framework notebooks."""
        root_dir = Path(__file__).parent.parent
        notebook_paths = []
        
        # Find all lesson directories
        for lesson_dir in root_dir.glob("*/code_samples/*.ipynb"):
            if "python-agent-framework" in lesson_dir.name:
                notebook_paths.append(lesson_dir)
        
        return notebook_paths
    
    def test_notebook_syntax(self, notebook_paths):
        """Test that all notebooks have valid syntax."""
        for notebook_path in notebook_paths:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            
            # Check that notebook can be parsed
            assert nb.cells, f"Notebook {notebook_path} has no cells"
            
            # Check that code cells have valid Python syntax
            for i, cell in enumerate(nb.cells):
                if cell.cell_type == 'code':
                    try:
                        compile(cell.source, f"{notebook_path}:cell_{i}", 'exec')
                    except SyntaxError as e:
                        pytest.fail(f"Syntax error in {notebook_path}, cell {i}: {e}")
    
    @pytest.mark.slow
    def test_notebook_execution(self, notebook_paths, mock_env_vars, mock_azure_credentials):
        """Test that notebooks can execute without errors (marked as slow test)."""
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        
        for notebook_path in notebook_paths:
            # Skip certain notebooks that require external services
            if any(skip in str(notebook_path) for skip in ['05-agentic-rag', '11-agentic-protocols']):
                pytest.skip(f"Skipping {notebook_path} - requires external services")
            
            with open(notebook_path, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            
            try:
                # Execute notebook
                ep.preprocess(nb, {'metadata': {'path': str(notebook_path.parent)})
            except CellExecutionError as e:
                pytest.fail(f"Execution error in {notebook_path}: {e}")
            except Exception as e:
                pytest.fail(f"Unexpected error in {notebook_path}: {e}")
    
    def test_notebook_metadata(self, notebook_paths):
        """Test that notebooks have required metadata."""
        for notebook_path in notebook_paths:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)
            
            # Check for required metadata
            assert nb.metadata, f"Notebook {notebook_path} missing metadata"
            
            # Check for kernel specification
            if 'kernelspec' not in nb.metadata:
                pytest.warn(f"Notebook {notebook_path} missing kernelspec metadata")


class TestNotebookStructure:
    """Test notebook structure and content."""
    
    def test_lesson_01_notebook_structure(self):
        """Test that lesson 01 notebook has expected structure."""
        notebook_path = Path(__file__).parent.parent / "01-intro-to-ai-agents/code_samples/01-python-agent-framework.ipynb"
        
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Check for expected cells
        cell_contents = [cell.source for cell in nb.cells if cell.cell_type == 'code']
        
        # Should import agent_framework
        import_found = any('agent_framework' in content for content in cell_contents)
        assert import_found, "Lesson 01 notebook should import agent_framework"
        
        # Should have tool definition
        tool_found = any('@tool' in content for content in cell_contents)
        assert tool_found, "Lesson 01 notebook should define a tool"
    
    def test_lesson_04_notebook_structure(self):
        """Test that lesson 04 notebook has expected structure."""
        notebook_path = Path(__file__).parent.parent / "04-tool-use/code_samples/04-python-agent-framework.ipynb"
        
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Check for expected cells
        cell_contents = [cell.source for cell in nb.cells if cell.cell_type == 'code']
        
        # Should import pydantic
        pydantic_found = any('pydantic' in content for content in cell_contents)
        assert pydantic_found, "Lesson 04 notebook should import pydantic"
        
        # Should have multiple tool definitions
        tool_count = sum(content.count('@tool') for content in cell_contents)
        assert tool_count >= 3, "Lesson 04 notebook should define multiple tools"
