class Logger:

    @staticmethod
    def titulo(texto):

        print("\n" + "=" * 60)
        print(texto)
        print("=" * 60)

    @staticmethod
    def exito(texto):

        print(f"✅ {texto}")

    @staticmethod
    def info(texto):

        print(f"ℹ️ {texto}")

    @staticmethod
    def error(texto):

        print(f"❌ {texto}")