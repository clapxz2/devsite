#!/usr/bin/env python3
"""
Local preview server for dev showcase website.
Starts a simple HTTP server to preview your site locally.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def start_preview_server(port=3000):
    """Start a local HTTP server for previewing the site."""
    # Change to the directory containing this script
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Create server
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"🚀 Starting preview server...")
            print(f"📱 Server running at: http://localhost:{port}")
            print(f"📁 Serving files from: {script_dir}")
            print(f"🌐 Opening browser...")
            print(f"⏹️  Press Ctrl+C to stop the server")
            print("=" * 50)
            
            # Open browser
            webbrowser.open(f'http://localhost:{port}')
            
            # Start server
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print(f"\n🛑 Server stopped by user")
        sys.exit(0)
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"❌ Port {port} is already in use. Try a different port:")
            print(f"   python preview.py {port + 1}")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)

def main():
    """Main function to handle command line arguments."""
    port = 3000
    
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number. Using default port 3000.")
    
    start_preview_server(port)

if __name__ == "__main__":
    main()
