from .downloader import GitHubDownloader
import sys

def main():
    """
    CLI entry point for the script.
    """
    if len(sys.argv) < 2:
        print("Usage: GitHubDownloader <GitHub URL>")
        sys.exit(1)
    url = sys.argv[1]
    try:
        downloader = GitHubDownloader(url=url)
        downloader.download()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

