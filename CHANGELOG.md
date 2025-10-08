# Changelog

All notable changes to MarkdownViewer will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-03

### Added
- **Dual-pane editor** with live Markdown preview
- **Native PDF export** using ReportLab (no external dependencies)
- **DOCX export** compatible with Microsoft Word
- **HTML export** with embedded CSS styling
- Full Markdown syntax support:
  - Headings (H1-H6)
  - Bold, italic, code inline
  - Lists (ordered and unordered)
  - Tables
  - Code blocks with syntax highlighting
  - Images and links
  - Horizontal rules
- **Keyboard shortcuts**:
  - `Ctrl+N` - New file
  - `Ctrl+O` - Open file
  - `Ctrl+S` - Save file
  - `Ctrl+B` - Bold
  - `Ctrl+I` - Italic
  - `Ctrl+K` - Code inline
  - `F5` - Toggle edit/view mode
  - `F6` - Split view
- **Auto-save** functionality (every 60 seconds)
- **Multiple view modes**: Split view, Editor only, Preview only
- **Font customization** for editor
- **Toolbar** with quick access buttons
- **Cross-platform support**: Windows, Linux, macOS
- **Standalone executables**: No Python installation required
- **GitHub Pages** documentation site

### Features
- Real-time preview updates (500ms delay after typing stops)
- Customizable markdown rendering with GitHub-style CSS
- Clean, modern UI using PyQt6
- Responsive layout
- File change detection
- Confirmation dialogs for unsaved changes

### Technical
- Built with PyQt6 for native desktop experience
- ReportLab for PDF generation
- python-docx for Word export
- Markdown library with multiple extensions
- PyInstaller for executable packaging
- MIT License

### Documentation
- Comprehensive README with installation instructions
- GitHub Pages website with features showcase
- Build system for creating installers
- Support for Windows (NSIS), Linux (.deb), macOS (.dmg)

## [Unreleased]

### Planned Features
- [ ] Syntax highlighting in code blocks
- [ ] Search and replace functionality
- [ ] Dark/light theme toggle
- [ ] Table of contents panel
- [ ] Export to additional formats (ODT, RTF, LaTeX)
- [ ] Spell checker
- [ ] Word count
- [ ] Templates support
- [ ] Plugin system

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Links

- [GitHub Repository](https://github.com/Yatrogenesis/MarkdownViewer)
- [GitHub Pages](https://yatrogenesis.github.io/MarkdownViewer/)
- [Issues](https://github.com/Yatrogenesis/MarkdownViewer/issues)
- [Releases](https://github.com/Yatrogenesis/MarkdownViewer/releases)

## 1.0.1 - PDF export fix
- Prefer Qt WebEngine printToPdf (faithful to preview).
- Fallback to ReportLab when WebEngine is unavailable or fails.
- Updated README to remove wkhtmltopdf guidance.
