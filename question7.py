class Engine:
    def start(self):
        pass

    def stop(self):
        pass

class Car(Engine):
    def __init__(self):
        # Composition: Car has an Engine instance
        self.engine = Engine()

    def start_engine(self):
        # Using Engine's start method through the Car instance
        self.engine.start()
        print(f"Car Engine started.")

    def stop_engine(self):
        # Using Engine's stop method through the Car instance
        self.engine.stop()
        print(f"Car Engine stopped.")

# Demonstrate the composition
car1 = Car()
# Starts the engine
car1.start_engine()
# Stops the engine
car1.stop_engine()
