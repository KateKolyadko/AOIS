class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        step = 1
        while self.buckets[index]:
            if self.buckets[index][0] == key:
                self.buckets[index][1] = value  
                return
            index = (index + step**2) % self.size  
            step += 1
        self.buckets[index] = [key, value]

    def get(self, key):
        index = self.hash(key)
        step = 1
        while self.buckets[index]:
            if self.buckets[index][0] == key:
                return self.buckets[index][1]
            index = (index + step**2) % self.size
            step += 1
        raise KeyError(key)

    def delete(self, key):
        index = self.hash(key)
        step = 1
        while self.buckets[index]:
            if self.buckets[index][0] == key:
                self.buckets[index] = []
                return
            index = (index + step**2) % self.size  # Квадратичный поиск
            step += 1
        raise KeyError(key)

    def __len__(self):
        return sum(len(bucket) for bucket in self.buckets if bucket)

    def clear(self):
        self.buckets = [[] for _ in range(self.size)]

    def load_factor(self):
        return len(self) / self.size

    def display(self):
        print("Содержимое хеш-таблицы:")
        for i, bucket in enumerate(self.buckets):
            if bucket:
                key, value = bucket
                v_k = hash(key) % self.size
                h_v = i
                print(f"Ключ: {key}, Значение: {value}, V(K): {v_k}, h(V): {h_v}")
        print(f"Коэффициент заполнения: {self.load_factor():.2f}")

biology = HashTable()

biology.insert("ДНК", "Дезоксирибонуклеиновая кислота, самовоспроизводящийся материал, "
                      "который присутствует практически во всех живых организмах в качестве основного "
                      "компонента генетического материала.")
biology.insert("Фотосинтез", "Процесс, с помощью которого растения и некоторые другие организмы "
                              "используют солнечный свет, воду и углекислый газ для создания кислорода и "
                              "энергии в виде сахара.")
biology.insert("Митоз", "Процесс деления клетки, в результате которого образуются две "
                         "генетически идентичные дочерние клетки.")
biology.insert("Экосистема", "Сообщество живых организмов (растений, животных и микробов), "
                              "взаимодействующих друг с другом и с их физической средой.")

print(biology.get("ДНК"))
print(len(biology))
biology.delete("Фотосинтез")
print(len(biology))
biology.display()