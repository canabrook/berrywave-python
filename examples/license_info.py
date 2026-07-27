from berrywave import EdiService


def main():
    service = EdiService()
    print(service.license_info())

if __name__ == "__main__":
    main()