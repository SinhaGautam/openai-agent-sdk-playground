import sys
import asyncio

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [joke|sales]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "joke":
        from runners.run_joke import run

    elif command == "sales":
        from runners.run_sales import run        

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

    asyncio.run(run())


if __name__ == "__main__":
    main()