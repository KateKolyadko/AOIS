class HashTable:
    def __init__(self):
        self.size = 10
        self.hash_table = [[] for _ in range(self.size)]

    def hashing(self, hash_key):
        return hash(hash_key) % self.size

    def insert(self, hash_key, value):
        i = self.hashing(hash_key)
        step = 1
        while self.hash_table[i]:
            if self.hash_table[i][0] == hash_key:
                self.hash_table[i][1] = value
                return
            index = (i + step**2) % self.size
            step += 1
        self.hash_table[i] = [hash_key, value]

    def get_by_key(self, hash_key):
        i = self.hashing(hash_key)
        step = 1
        while self.hash_table[i]:
            if self.hash_table[i][0] == hash_key:
                return self.hash_table[i][1]
            i = (i + step**2) % self.size
            step += 1
        raise KeyError(hash_key)

    def delete_by_key(self, hash_key):
        i = self.hashing(hash_key)
        j = 1
        while self.hash_table[i]:
            if self.hash_table[i][0] == hash_key:
                self.hash_table[i] = []
                return
            i = (i + j**2) % self.size
            j += 1
        raise KeyError(hash_key)

    def __len__(self):
        return sum(len(table_row) for table_row in self.hash_table if table_row)

    def clear_hash_table(self):
        self.hash_table = [[] for _ in range(self.size)]

    def get_load_factor(self):
        return len(self) / self.size

    def print_hash_table(self):
        print("Содержимое хеш-таблицы:")
        for i, table_row in enumerate(self.hash_table):
            if table_row:
                hash_key, hash_value = table_row
                v_k = hash(hash_key) % self.size
                h_v = i
                print(f"Ключ: {hash_key}, Значение: {hash_value}, V(K): {v_k}, h(V): {h_v}")
        print(f"Коэффициент заполнения: {self.get_load_factor():.2f}")

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

print(biology.get_by_key("ДНК"))
print(len(biology))
biology.delete_by_key("Фотосинтез")
print(len(biology))
biology.print_hash_table()