import xmlrpc.client
import argparse

RED = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def banner():
    banners = """
    ██╗  ██╗███╗   ███╗██╗     ██████╗ ██████╗  ██████╗     █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
    ╚██╗██╔╝████╗ ████║██║     ██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
     ╚███╔╝ ██╔████╔██║██║     ██████╔╝██████╔╝██║         ███████║   ██║      ██║   ███████║██║     █████╔╝ 
     ██╔██╗ ██║╚██╔╝██║██║     ██╔══██╗██╔═══╝ ██║         ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
    ██╔╝ ██╗██║ ╚═╝ ██║███████╗██║  ██║██║     ╚██████╗    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
    ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   """
    
    info = """
    Author: ForwardEcho
    Version: 1.0
    Description: Simple XML-RPC client for testing purposes. """
    print()
    print(RED + banners + RESET)
    print(BLUE + info + RESET)
    print()
def create_proxy(server_url):
    try:
        proxy = xmlrpc.client.ServerProxy(server_url)
        # Test connection
        proxy.system.listMethods()
        return proxy
    except Exception as e:
        print(f"{RED}Error:{RESET} Failed to connect to server: {e}")
        exit(1)

def getMethods(proxy):
    try:
        methods = proxy.system.listMethods()
        print("Available methods:")
        for i, method in enumerate(methods, 1):
            print(f"{i}. {GREEN}{method}{RESET}")
    except Exception as e:
        print(f"{RED}Error:{RESET} Unable to retrieve methods: {e}")

def callMethod(proxy, method, params):
    try:
        result = getattr(proxy, method)(*params) if params else getattr(proxy, method)()
        print(f"{BLUE}Result of '{method}':{RESET} {result}")
    except xmlrpc.client.Fault as fault:
        print(f"{RED}Error:{RESET} {fault.faultString}")
    except AttributeError:
        print(f"{RED}Error:{RESET} Method '{method}' not found.")
    except Exception as e:
        print(f"{RED}Unexpected error:{RESET} {e}")

if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(description="XML-RPC client")
    parser.add_argument("-u", "--url", required=True, help="URL of the XML-RPC server")
    parser.add_argument("-l", "--list", action="store_true", help="List available methods")
    parser.add_argument("-m", "--method", help="Method to call")
    parser.add_argument("params", nargs="*", help="Parameters for the method (optional)")
    args = parser.parse_args()

    proxy = create_proxy(args.url)

    if args.list:
        getMethods(proxy)
    elif args.method:
        params = args.params if args.params else []
        callMethod(proxy, args.method, params)
    else:
        print(f"{YELLOW}Please specify either --list/-l to list methods or --method/-m to call a method.{RESET}")
