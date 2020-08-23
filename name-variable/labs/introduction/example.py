def main():
    # "__name__" value depending on how we execute the containing script
    print("__name__       = %s" % __name__)
    print("type(__name__) = %s" % type(__name__))


# This means that if this script is executed,
# then "main()" will be executed
if __name__ == "__main__":
    main()
