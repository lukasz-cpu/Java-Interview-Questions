# Java Developer Interview Preparation - Kompleksowe Notatki

## Spis treści

1. [Algorytmy i Struktury Danych](#algorytmy-i-struktury-danych)
2. [Podstawy Java](#podstawy-java)
3. [Bazy Danych](#bazy-danych)
4. [Wzorce Projektowe](#wzorce-projektowe)
5. [Spring Framework](#spring-framework)
6. [Współbieżność i Threading](#współbieżność-i-threading)
7. [Architektura i Mikroserwisy](#architektura-i-mikroserwisy)
8. [REST API i Protokoły](#rest-api-i-protokoły)
9. [Bezpieczeństwo](#bezpieczeństwo)
10. [Testowanie](#testowanie)
11. [Dodatkowe Tematy](#dodatkowe-tematy)

---

## 1. Algorytmy i Struktury Danych

### 1.1 Ciąg Fibonacciego

**Definicja:** Ciąg Fibonacciego to ciąg liczbowy gdzie każda liczba jest sumą dwóch poprzednich: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

```java
public class Fibonacci {
    public static void main(String[] args) {
        int n = 10; // liczba elementów ciągu
        int a = 0, b = 1, c;

        System.out.print("Ciąg Fibonacciego " + n + " elementów: ");

        for (int i = 1; i <= n; i++) {
            System.out.print(a + " ");
            c = a + b;
            a = b;
            b = c;
        }
    }
}
```

**Złożoność czasowa:** O(n)
**Złożoność pamięciowa:** O(1)

**Alternatywne implementacje:**

- Rekurencyjna (O(2^n) - nieefektywna)
- Memoization (O(n) czas, O(n) pamięć)
- Matrix exponentiation (O(log n))

### 1.2 Generowanie liczb pierwszych

**Definicja:** Liczba pierwsza to liczba naturalna większa od 1, która ma dokładnie dwa dzielniki: 1 i siebie samą.

```java
public class PrimeNumbers {
    public static void main(String[] args) {
        for(int i = 2; i < 100; i++){
            if(isPrime(i)){
                System.out.println(i);
            }
        }
    }

    static boolean isPrime(int number) {
        if (number <= 1) return false;
        if (number == 2) return true;
        if (number % 2 == 0) return false;

        // Sprawdzamy tylko do pierwiastka z number
        for (int i = 3; i <= Math.sqrt(number); i += 2) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

**Ulepszenie z notatek:** Oryginalna implementacja ma złożoność O(n), można poprawić do O(√n).

**Sito Eratostenesa** - dla większych zakresów:

```java
public static List<Integer> sieveOfEratosthenes(int n) {
    boolean[] prime = new boolean[n + 1];
    Arrays.fill(prime, true);
    prime[0] = prime[1] = false;

    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p) {
                prime[i] = false;
            }
        }
    }

    List<Integer> primes = new ArrayList<>();
    for (int i = 2; i <= n; i++) {
        if (prime[i]) primes.add(i);
    }
    return primes;
}
```

### 1.3 Stack (Stos)

**Definicja:** LIFO (Last In, First Out) - struktura danych, gdzie ostatni dodany element jest pierwszym usuwanym.

**Podstawowe operacje:**

- **Push:** Dodaje element na wierzch stosu
- **Pop:** Usuwa i zwraca element z wierzchu stosu
- **Peek/Top:** Zwraca element z wierzchu bez usuwania
- **isEmpty:** Sprawdza czy stos jest pusty

```java
public class StackExample {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        // Push elements
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // Peek
        System.out.println("Top element: " + stack.peek()); // 30

        // Pop elements
        while (!stack.isEmpty()) {
            System.out.println("Popped: " + stack.pop());
        }
    }
}
```

**Aplikacje praktyczne:**

- Wywołania funkcji (call stack)
- Operacje cofnij/ponów (undo/redo)
- Nawigacja w przeglądarce
- Parsowanie wyrażeń matematycznych
- Sprawdzanie poprawności nawiasów

### 1.4 Queue (Kolejka)

**Definicja:** FIFO (First In, First Out) - struktura danych, gdzie pierwszy dodany element jest pierwszym usuwanym.

```java
public class QueueExample {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        // Enqueue (add)
        queue.add(10);
        queue.add(20);
        queue.add(30);

        // Dequeue (remove)
        while (!queue.isEmpty()) {
            System.out.println("Dequeued: " + queue.poll());
        }
    }
}
```

**Implementacje w Java:**

- **LinkedList:** Implementuje Queue interface
- **ArrayDeque:** Wydajniejsza implementacja
- **PriorityQueue:** Kolejka priorytetowa (nie FIFO)
- **PriorityBlockingQueue:** Thread-safe

**Aplikacje praktyczne:**

- Systemy kolejkowe (print spooler, CPU scheduling)
- BFS (Breadth-First Search)
- Producer-Consumer pattern
- Rate limiting

### 1.5 LinkedList vs ArrayList

| Cecha                  | ArrayList          | LinkedList                |
| ---------------------- | ------------------ | ------------------------- |
| Struktura              | Dynamiczna tablica | Podwójnie powiązana lista |
| Dostęp losowy          | O(1)               | O(n)                      |
| Wstawianie na początku | O(n)               | O(1)                      |
| Wstawianie na końcu    | O(1) amortized     | O(1)                      |
| Wstawianie w środku    | O(n)               | O(1) jeśli mamy iterator  |
| Usuniecie              | O(n)               | O(1) jeśli mamy iterator  |
| Zużycie pamięci        | Mniejsze           | Większe (pointers)        |

**Kiedy używać:**

- **ArrayList:** Częsty dostęp losowy, iteracja
- **LinkedList:** Częste wstawianie/usuwanie, implementacja Queue/Deque

### 1.6 Znajdowanie środkowego elementu LinkedList

**Problem:** Znajdź środkowy element w single-linked list w jednym przejściu.

**Rozwiązanie - Two Pointer Technique:**

```java
public ListNode findMiddle(ListNode head) {
    if (head == null) return null;

    ListNode slow = head;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow;
}
```

**Wyjaśnienie:** Fast pointer porusza się 2x szybciej. Gdy dotrze do końca, slow pointer będzie w środku.

---

## 2. Podstawy Java

### 2.1 Stack vs Heap

| Cecha            | Stack                             | Heap              |
| ---------------- | --------------------------------- | ----------------- |
| Przechowuje      | Zmienne lokalne, parametry metod  | Obiekty, arrays   |
| Zarządzanie      | Automatyczne (scope-based)        | Garbage Collector |
| Szybkość dostępu | Szybszy                           | Wolniejszy        |
| Rozmiar          | Mniejszy, ograniczony             | Większy           |
| Threading        | Thread-safe (każdy wątek ma swój) | Współdzielony     |
| Błędy            | StackOverflowError                | OutOfMemoryError  |

**Przykład:**

```java
public void method() {
    int x = 10;           // Stack
    String name = "John"; // Stack (referencja)
    Person p = new Person(); // Stack (referencja) -> Heap (obiekt)
}
```

### 2.2 String Pool

**Definicja:** String Pool to specjalny obszar w heap memory gdzie JVM przechowuje String literals aby oszczędzić pamięć.

```java
public class StringPoolExample {
    public static void main(String[] args) {
        String s1 = "Hello";        // String Pool
        String s2 = "Hello";        // Referencja do tego samego obiektu
        String s3 = new String("Hello"); // Nowy obiekt w heap

        System.out.println(s1 == s2);       // true
        System.out.println(s1 == s3);       // false
        System.out.println(s1.equals(s3));  // true

        // Intern() - dodaje string do pool lub zwraca istniejący
        String s4 = s3.intern();
        System.out.println(s1 == s4);       // true
    }
}
```

**Korzyści:**

- Oszczędność pamięci
- Szybsze porównania referencji
- Immutability stringsów

### 2.3 StringBuilder vs StringBuffer

| Cecha          | StringBuilder | StringBuffer         |
| -------------- | ------------- | -------------------- |
| Thread-safe    | NIE           | TAK                  |
| Wydajność      | Szybszy       | Wolniejszy           |
| Synchronizacja | Brak          | Synchronized methods |
| Wprowadzenie   | Java 5        | Java 1.0             |

```java
public class StringBuilderVsBuffer {
    public static void main(String[] args) {
        // StringBuilder - single-threaded
        StringBuilder sb = new StringBuilder();
        sb.append("Hello").append(" ").append("World");

        // StringBuffer - multi-threaded
        StringBuffer sbf = new StringBuffer();
        sbf.append("Hello").append(" ").append("World");
    }
}
```

**Kiedy używać:**

- **StringBuilder:** Single-threaded aplikacje (większość przypadków)
- **StringBuffer:** Multi-threaded środowiska gdzie potrzebujemy thread-safety

### 2.4 Type Erasure (Generics)

**Definicja:** Mechanizm w Javie gdzie informacje o typach generycznych są usuwane podczas kompilacji dla zachowania wstecznej kompatybilności.

```java
// Przed kompilacją
List<String> stringList = new ArrayList<String>();
List<Integer> intList = new ArrayList<Integer>();

// Po kompilacji (bytecode)
List stringList = new ArrayList();
List intList = new ArrayList();
```

**Konsekwencje:**

```java
public class TypeErasureExample {
    public static void main(String[] args) {
        List<String> strings = new ArrayList<>();
        List<Integer> integers = new ArrayList<>();

        // Oba mają ten sam Class object
        System.out.println(strings.getClass() == integers.getClass()); // true

        // Nie można przeciążyć metod różniących się tylko generic types
        // public void method(List<String> list) { } // ERROR
        // public void method(List<Integer> list) { } // ERROR
    }
}
```

### 2.5 Typy referencji w Java

#### 2.5.1 Strong References (Silne referencje)

**Definicja:** Domyślny typ referencji. Obiekty nie są eligible do GC dopóki istnieją strong references.

```java
MyClass obj = new MyClass(); // Strong reference
obj = null; // Teraz obiekt jest eligible do GC
```

#### 2.5.2 Weak References (Słabe referencje)

**Definicja:** Nie zapobiegają garbage collection. Useful dla cache implementations.

```java
import java.lang.ref.WeakReference;

public class WeakReferenceExample {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
        WeakReference<MyClass> weakRef = new WeakReference<>(obj);

        obj = null; // Usuń strong reference
        System.gc(); // Suggest GC

        if (weakRef.get() == null) {
            System.out.println("Object was garbage collected");
        }
    }
}
```

#### 2.5.3 Soft References (Miękkie referencje)

**Definicja:** Podobne do weak, ale GC usuwa je tylko gdy brakuje pamięci.

```java
import java.lang.ref.SoftReference;

SoftReference<MyClass> softRef = new SoftReference<>(new MyClass());
// Obiekt zostanie usunięty tylko gdy JVM potrzebuje pamięci
```

#### 2.5.4 Phantom References (Fantomowe referencje)

**Definicja:** Używane do cleanup operations. Obiekt jest już "dead" ale można wykonać cleanup.

```java
import java.lang.ref.PhantomReference;
import java.lang.ref.ReferenceQueue;

ReferenceQueue<MyClass> queue = new ReferenceQueue<>();
PhantomReference<MyClass> phantomRef = new PhantomReference<>(new MyClass(), queue);
```

### 2.6 Exceptions w Java

**Hierarchia:**

```
Throwable
├── Error (OutOfMemoryError, StackOverflowError)
└── Exception
    ├── RuntimeException (Unchecked)
    │   ├── NullPointerException
    │   ├── IllegalArgumentException
    │   └── ClassCastException
    └── Checked Exceptions
        ├── IOException
        ├── SQLException
        └── ClassNotFoundException
```

#### Checked vs Unchecked Exceptions

**Checked Exceptions:**

- Muszą być obsłużone lub zadeklarowane
- Sprawdzane podczas kompilacji
- Np. IOException, SQLException

```java
public void readFile() throws IOException {
    FileReader file = new FileReader("file.txt");
}
```

**Unchecked Exceptions (Runtime):**

- Nie muszą być obsłużone
- Dziedziczą po RuntimeException
- Np. NullPointerException, IllegalArgumentException

```java
public class ValidationException extends RuntimeException {
    public ValidationException(String message) {
        super(message);
    }
}
```

#### Extending Exception vs RuntimeException

**Extending Exception (Checked):**

```java
public class ValidationException extends Exception {
    // Musi być caught lub declared
}
```

**Extending RuntimeException (Unchecked):**

```java
public class ValidationException extends RuntimeException {
    // Opcjonalne catch/declare
}
```

**Kiedy używać:**

- **Checked:** Błędy, które client może odzyskać (file not found)
- **Unchecked:** Programming errors (null pointer, illegal argument)

### 2.7 Comparable vs Comparator

| Cecha         | Comparable       | Comparator              |
| ------------- | ---------------- | ----------------------- |
| Package       | java.lang        | java.util               |
| Metoda        | compareTo(T o)   | compare(T o1, T o2)     |
| Sorting       | Natural ordering | Custom ordering         |
| Implementacja | W klasie obiektu | Zewnętrzna klasa/lambda |
| Ilość         | Jedna na klasę   | Wiele możliwych         |

**Comparable Example:**

```java
public class Person implements Comparable<Person> {
    private String name;
    private int age;

    @Override
    public int compareTo(Person other) {
        return this.name.compareTo(other.name);
    }
}
```

**Comparator Example:**

```java
// Lambda expression
Comparator<Person> byAge = (p1, p2) -> Integer.compare(p1.getAge(), p2.getAge());

// Method reference
Comparator<Person> byName = Comparator.comparing(Person::getName);

// Multiple criteria
Comparator<Person> byNameThenAge = Comparator
    .comparing(Person::getName)
    .thenComparing(Person::getAge);

Collections.sort(people, byAge);
```

### 2.8 Testowanie prywatnych metod

**Problem:** Czy można testować prywatne metody?

**Odpowiedź:** Technicznie tak (reflection), ale generalnie nie powinno się tego robić.

**Reflection approach:**

```java
import java.lang.reflect.Method;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MyClassTest {
    @Test
    public void testPrivateMethod() throws Exception {
        MyClass myObject = new MyClass();
        Method privateMethod = MyClass.class.getDeclaredMethod("privateMethod", int.class);
        privateMethod.setAccessible(true);
        int result = (int) privateMethod.invoke(myObject, 3);
        assertEquals(6, result);
    }
}
```

**Dlaczego tego unikać:**

1. **Brittle tests** - testy są związane z implementacją
2. **Refactoring problems** - zmiana nazwy metody psuje testy
3. **Testing philosophy** - test powinien testować behavior, nie implementation

**Lepsze podejście:**

1. Test through public methods
2. Extract private method to separate class
3. Use package-private visibility if testing is needed

### 2.9 Java 8 Functional Interfaces

**Definicja:** Interface z dokładnie jedną abstract method (SAM - Single Abstract Method).

**Główne typy:**

#### Consumer<T>

```java
Consumer<String> printer = s -> System.out.println(s);
printer.accept("Hello World");
```

#### Supplier<T>

```java
Supplier<String> supplier = () -> "Hello World";
String result = supplier.get();
```

#### Function<T, R>

```java
Function<String, Integer> length = s -> s.length();
Integer len = length.apply("Hello");
```

#### Predicate<T>

```java
Predicate<String> isEmpty = s -> s.isEmpty();
boolean result = isEmpty.test("");
```

#### BiFunction<T, U, R>

```java
BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;
Integer sum = add.apply(5, 3);
```

### 2.10 HashMap - Jak działa wewnętrznie

**Struktura:**

- Array of buckets (Node<K,V>[] table)
- Each bucket can contain single node or linked list/red-black tree
- Default capacity: 16, Load factor: 0.75

**Hash Function:**

```java
static final int hash(Object key) {
    int h;
    return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
```

**Put Operation:**

1. Oblicz hash code klucza
2. Znajdź bucket: `index = (n-1) & hash`
3. Jeśli bucket pusty - dodaj nowy node
4. Jeśli collision - użyj linked list lub tree
5. Jeśli przekroczony load factor - resize

**Java 8 Optimization:**

- Jeśli linked list ma ≥8 elementów → konwersja do red-black tree
- Jeśli tree ma ≤6 elementów → konwersja do linked list

**Bucket:**

```java
static class Node<K,V> implements Map.Entry<K,V> {
    final int hash;
    final K key;
    V value;
    Node<K,V> next;
}
```

### 2.11 HashSet vs LinkedHashSet vs TreeSet

| Feature        | HashSet  | LinkedHashSet   | TreeSet        |
| -------------- | -------- | --------------- | -------------- |
| Ordering       | No order | Insertion order | Sorted order   |
| Performance    | O(1)     | O(1)            | O(log n)       |
| Implementation | HashMap  | LinkedHashMap   | Red-Black Tree |
| Null values    | One null | One null        | No nulls       |
| Interface      | Set      | Set             | NavigableSet   |

```java
public class SetComparison {
    public static void main(String[] args) {
        Set<String> hashSet = new HashSet<>();
        Set<String> linkedHashSet = new LinkedHashSet<>();
        Set<String> treeSet = new TreeSet<>();

        String[] elements = {"banana", "apple", "cherry"};

        for (String element : elements) {
            hashSet.add(element);
            linkedHashSet.add(element);
            treeSet.add(element);
        }

        System.out.println("HashSet: " + hashSet);        // Random order
        System.out.println("LinkedHashSet: " + linkedHashSet); // banana, apple, cherry
        System.out.println("TreeSet: " + treeSet);        // apple, banana, cherry
    }
}
```

### 2.12 HashMap vs LinkedHashMap vs TreeMap

| Feature        | HashMap      | LinkedHashMap            | TreeMap           |
| -------------- | ------------ | ------------------------ | ----------------- |
| Ordering       | No order     | Insertion/Access order   | Key-based sorting |
| Performance    | O(1)         | O(1)                     | O(log n)          |
| Implementation | Hash table   | Hash table + linked list | Red-Black Tree    |
| Null keys      | One null key | One null key             | No null keys      |
| Interface      | Map          | Map                      | NavigableMap      |

```java
Map<String, Integer> hashMap = new HashMap<>();
Map<String, Integer> linkedHashMap = new LinkedHashMap<>();
Map<String, Integer> treeMap = new TreeMap<>();

// LinkedHashMap with access-order
Map<String, Integer> accessOrderMap = new LinkedHashMap<>(16, 0.75f, true);
```

**TreeMap sorting:**

```java
// Natural ordering (Comparable)
TreeMap<String, Integer> treeMap = new TreeMap<>();

// Custom ordering (Comparator)
TreeMap<String, Integer> customTreeMap = new TreeMap<>(String.CASE_INSENSITIVE_ORDER);
```

### 2.13 Volatile vs Synchronized

| Feature     | volatile            | synchronized       |
| ----------- | ------------------- | ------------------ |
| Level       | Variable level      | Method/Block level |
| Locking     | No locking          | Locking mechanism  |
| Atomicity   | Simple reads/writes | Complex operations |
| Performance | Faster              | Slower             |
| Visibility  | Guaranteed          | Guaranteed         |
| Use case    | Flags, status       | Critical sections  |

**Volatile Example:**

```java
public class VolatileExample {
    private volatile boolean running = true;

    public void stop() {
        running = false; // Visible to all threads immediately
    }

    public void doWork() {
        while (running) {
            // Work...
        }
    }
}
```

**Synchronized Example:**

```java
public class SynchronizedExample {
    private int counter = 0;

    public synchronized void increment() {
        counter++; // Atomic operation
    }

    public synchronized int getCounter() {
        return counter;
    }
}
```

**Kiedy używać:**

- **volatile:** Simple flags, status variables, publish-subscribe scenarios
- **synchronized:** Complex operations, multiple variables, atomicity requirements

---

## 3. Bazy Danych

### 3.1 ACID Properties

**ACID** to zestaw właściwości gwarantujących niezawodność transakcji bazodanowych:

#### Atomicity (Atomowość)

- Transakcja jest niepodzielna - albo wykonuje się w całości, albo wcale
- Jeśli jakakolwiek operacja w transakcji niepowiedzie się, cała transakcja jest cofana

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
-- Jeśli którykolwiek UPDATE niepowiedzie się, oba są cofane
COMMIT;
```

#### Consistency (Spójność)

- Transakcja przeprowadza bazę z jednego spójnego stanu w inny
- Wszystkie constraints, triggers, cascades muszą być spełnione

#### Isolation (Izolacja)

- Równoczesne transakcje nie wpływają na siebie
- Poziomy izolacji: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE

#### Durability (Trwałość)

- Raz zatwierdzone zmiany są permanentne, nawet w przypadku awarii systemu
- Dane są zapisane na stałym nośniku

### 3.2 Transaction Isolation Levels

#### READ UNCOMMITTED (Najmniej restrykcyjny)

- Pozwala na dirty reads
- Transakcja może czytać niezatwierdzone zmiany z innych transakcji

#### READ COMMITTED (Domyślny w większości DB)

- Zapobiega dirty reads
- Transakcja widzi tylko zatwierdzone zmiany
- Może wystąpić non-repeatable read

#### REPEATABLE READ

- Zapobiega dirty reads i non-repeatable reads
- Wielokrotne czytanie tego samego wiersza zwraca ten sam wynik
- Może wystąpić phantom read

#### SERIALIZABLE (Najbardziej restrykcyjny)

- Najwyższy poziom izolacji
- Zapobiega wszystkim anomaliom
- Wykonuje transakcje sekwencyjnie

```java
@Transactional(isolation = Isolation.READ_COMMITTED)
public void updateAccount(Long id, BigDecimal amount) {
    // Transaction logic
}
```

### 3.3 Anomalie w SQL (Phenomena)

#### Dirty Read

Transakcja czyta dane zmienione przez inną niezatwierdzoną transakcję.

```sql
-- Transaction 1
BEGIN;
UPDATE accounts SET balance = 1000 WHERE id = 1;
-- Nie committed jeszcze

-- Transaction 2 (w tym samym czasie)
SELECT balance FROM accounts WHERE id = 1; -- Może zobaczyć 1000 (dirty read)
```

#### Non-Repeatable Read

Transakcja czyta ten sam wiersz dwukrotnie i otrzymuje różne wyniki.

```sql
-- Transaction 1
BEGIN;
SELECT balance FROM accounts WHERE id = 1; -- balance = 500

-- Transaction 2 commits update
UPDATE accounts SET balance = 1000 WHERE id = 1;
COMMIT;

-- Transaction 1 continues
SELECT balance FROM accounts WHERE id = 1; -- balance = 1000 (różny wynik)
```

#### Phantom Read

Transakcja wykonuje to samo zapytanie dwukrotnie i otrzymuje różną liczbę wierszy.

```sql
-- Transaction 1
BEGIN;
SELECT COUNT(*) FROM accounts WHERE balance > 500; -- Count = 5

-- Transaction 2 inserts new record
INSERT INTO accounts (balance) VALUES (600);
COMMIT;

-- Transaction 1 continues
SELECT COUNT(*) FROM accounts WHERE balance > 500; -- Count = 6 (phantom)
```

#### Serialization Anomaly

Wynik zatwierdzenia grupy transakcji jest niespójny z jakimkolwiek sekwencyjnym wykonaniem.

### 3.4 Primary Key

**Definicja:** Kolumna lub kombinacja kolumn, które jednoznacznie identyfikują każdy wiersz w tabeli.

**Właściwości:**

- Unique - nie może mieć duplikatów
- Not null - nie może być puste
- Immutable - nie powinno się zmieniać
- Minimal - jak najmniej kolumn

**Typy:**

#### Natural Key

Klucz pochodzący z danych biznesowych

```sql
CREATE TABLE countries (
    country_code CHAR(2) PRIMARY KEY, -- 'US', 'PL'
    name VARCHAR(100)
);
```

#### Surrogate Key

Sztuczny klucz bez znaczenia biznesowego

```sql
CREATE TABLE users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(100)
);
```

#### Composite Key

Klucz składający się z wielu kolumn

```sql
CREATE TABLE order_items (
    order_id BIGINT,
    product_id BIGINT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);
```

### 3.5 Indeksy w bazach danych

**Definicja:** Struktury danych, które przyspieszają wyszukiwanie kosztem dodatkowego miejsca i wolniejszych operacji INSERT/UPDATE/DELETE.

**Typy indeksów:**

#### Clustered Index

- Dane są fizycznie sortowane według klucza indeksu
- Jeden na tabelę (zwykle primary key)
- Leaf nodes zawierają rzeczywiste dane

#### Non-Clustered Index

- Wskazuje na lokalizację danych
- Wiele może istnieć na jednej tabeli
- Leaf nodes zawierają wskaźniki do danych

```sql
-- Tworzenie indeksu
CREATE INDEX idx_user_email ON users(email);

-- Indeks kompozytowy
CREATE INDEX idx_order_date_status ON orders(order_date, status);

-- Indeks unique
CREATE UNIQUE INDEX idx_user_email_unique ON users(email);

-- Usuwanie indeksu
DROP INDEX idx_user_email;
```

**Kiedy używać indeksów:**

- Kolumny w WHERE clause
- Kolumny w JOIN conditions
- Kolumny w ORDER BY
- Foreign keys

**Kiedy unikać:**

- Małe tabele
- Kolumny często modyfikowane
- Tabele z dużą liczbą INSERT/UPDATE/DELETE

### 3.6 JOIN Operations

#### INNER JOIN

Zwraca wiersze, które mają dopasowania w obu tabelach.

```sql
SELECT c.name, o.order_date
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id;
```

#### LEFT JOIN (LEFT OUTER JOIN)

Zwraca wszystkie wiersze z lewej tabeli + dopasowania z prawej.

```sql
SELECT c.name, o.order_date
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id;
```

#### RIGHT JOIN (RIGHT OUTER JOIN)

Zwraca wszystkie wiersze z prawej tabeli + dopasowania z lewej.

```sql
SELECT c.name, o.order_date
FROM customers c
RIGHT JOIN orders o ON c.id = o.customer_id;
```

#### FULL OUTER JOIN

Zwraca wszystkie wiersze z obu tabel.

```sql
SELECT c.name, o.order_date
FROM customers c
FULL OUTER JOIN orders o ON c.id = o.customer_id;
```

### 3.7 GROUP BY i HAVING

**GROUP BY** grupuje wyniki według określonych kolumn, umożliwiając agregację danych.

**HAVING** filtruje wyniki po grupowaniu (nie można użyć WHERE z funkcjami agregującymi).

```sql
-- GROUP BY example
SELECT product_category, SUM(sales) as total_sales
FROM sales_table
GROUP BY product_category;

-- HAVING example
SELECT product_category, SUM(sales) as total_sales
FROM sales_table
GROUP BY product_category
HAVING SUM(sales) > 100000;

-- Różnica WHERE vs HAVING
SELECT category, COUNT(*) as product_count
FROM products
WHERE price > 100  -- Filtruje przed grupowaniem
GROUP BY category
HAVING COUNT(*) > 5;  -- Filtruje po grupowaniu
```

### 3.8 UNION vs UNION ALL

**UNION** - łączy wyniki z dwóch lub więcej SELECT, usuwając duplikaty.
**UNION ALL** - łączy wyniki bez usuwania duplikatów (szybszy).

```sql
-- UNION (usuwa duplikaty)
SELECT name FROM customers
UNION
SELECT name FROM suppliers;

-- UNION ALL (zachowuje duplikaty)
SELECT name FROM customers
UNION ALL
SELECT name FROM suppliers;
```

**Wymagania:**

- Ta sama liczba kolumn
- Kompatybilne typy danych
- Ta sama kolejność kolumn

### 3.9 Partycjonowanie w bazach danych

**Definicja:** Dzielenie dużych tabel na mniejsze, łatwiejsze do zarządzania części.

#### Vertical Partitioning (Partycjonowanie pionowe)

Dzielenie tabeli na kolumny - często używane kolumny w jednej partycji.

```sql
-- Oryginalna tabela
CREATE TABLE users (
    id BIGINT,
    email VARCHAR(255),
    name VARCHAR(100),
    profile_data TEXT,
    last_login TIMESTAMP
);

-- Po partycjonowaniu pionowym
CREATE TABLE users_basic (
    id BIGINT,
    email VARCHAR(255),
    name VARCHAR(100)
);

CREATE TABLE users_extended (
    id BIGINT,
    profile_data TEXT,
    last_login TIMESTAMP
);
```

#### Horizontal Partitioning (Partycjonowanie poziome)

Dzielenie tabeli na wiersze według określonych kryteriów.

```sql
-- Partycjonowanie po dacie
CREATE TABLE orders_2023 (
    LIKE orders INCLUDING ALL
) INHERITS (orders);

CREATE TABLE orders_2024 (
    LIKE orders INCLUDING ALL
) INHERITS (orders);

-- Partycjonowanie po hashingu
CREATE TABLE users_partition_0 AS
SELECT * FROM users WHERE MOD(id, 4) = 0;

CREATE TABLE users_partition_1 AS
SELECT * FROM users WHERE MOD(id, 4) = 1;
```

**Korzyści:**

- Lepsze performance dla dużych tabel
- Łatwiejsze zarządzanie i maintenance
- Możliwość parallel processing
- Szybsze backup/restore

---

## 4. Wzorce Projektowe

### 4.1 Singleton Pattern

**Definicja:** Zapewnia, że klasa ma tylko jedną instancję i zapewnia globalny dostęp do niej.

#### Thread-Safe Implementation

```java
public class Singleton {
    private static volatile Singleton instance;

    private Singleton() {
        // Prywatny konstruktor zapobiega tworzeniu instancji
    }

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

#### Eager Initialization (Thread-safe by default)

```java
public class EagerSingleton {
    private static final EagerSingleton instance = new EagerSingleton();

    private EagerSingleton() {}

    public static EagerSingleton getInstance() {
        return instance;
    }
}
```

#### Bill Pugh Solution (Recommended)

```java
public class BillPughSingleton {
    private BillPughSingleton() {}

    private static class SingletonHelper {
        private static final BillPughSingleton INSTANCE = new BillPughSingleton();
    }

    public static BillPughSingleton getInstance() {
        return SingletonHelper.INSTANCE;
    }
}
```

#### Enum Singleton (Best approach)

```java
public enum SingletonEnum {
    INSTANCE;

    public void doSomething() {
        // Business logic
    }
}
```

### 4.2 Builder Pattern

**Definicja:** Konstruuje złożone obiekty krok po kroku, pozwalając na różne reprezentacje.

```java
public class Person {
    private final String name;
    private final int age;
    private final String address;
    private final String phone;
    private final String email;

    private Person(PersonBuilder builder) {
        this.name = builder.name;
        this.age = builder.age;
        this.address = builder.address;
        this.phone = builder.phone;
        this.email = builder.email;
    }

    public static class PersonBuilder {
        // Required parameters
        private final String name;
        private final int age;

        // Optional parameters
        private String address;
        private String phone;
        private String email;

        public PersonBuilder(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public PersonBuilder address(String address) {
            this.address = address;
            return this;
        }

        public PersonBuilder phone(String phone) {
            this.phone = phone;
            return this;
        }

        public PersonBuilder email(String email) {
            this.email = email;
            return this;
        }

        public Person build() {
            return new Person(this);
        }
    }

    // Getters...
}
```

**Użycie:**

```java
Person person = new Person.PersonBuilder("John Doe", 30)
    .address("123 Main St")
    .phone("555-555-1234")
    .email("john@example.com")
    .build();
```

**Korzyści:**

- Immutable objects
- Fluent API
- Walidacja w build()
- Opcjonalne parametry

### 4.3 Strategy Pattern

**Definicja:** Definiuje rodzinę algorytmów, enkapsuluje każdy z nich i czyni je wymiennymi.

```java
// Strategy interface
public interface PaymentStrategy {
    void pay(double amount);
}

// Concrete strategies
public class CreditCardPayment implements PaymentStrategy {
    private String name;
    private String cardNumber;
    private String cvv;
    private String dateOfExpiry;

    public CreditCardPayment(String name, String cardNumber, String cvv, String dateOfExpiry) {
        this.name = name;
        this.cardNumber = cardNumber;
        this.cvv = cvv;
        this.dateOfExpiry = dateOfExpiry;
    }

    @Override
    public void pay(double amount) {
        System.out.println(amount + " paid using credit card " + cardNumber);
    }
}

public class PayPalPayment implements PaymentStrategy {
    private String emailId;
    private String password;

    public PayPalPayment(String emailId, String password) {
        this.emailId = emailId;
        this.password = password;
    }

    @Override
    public void pay(double amount) {
        System.out.println(amount + " paid using PayPal account " + emailId);
    }
}

public class BankTransferPayment implements PaymentStrategy {
    private String accountNumber;
    private String routingNumber;

    public BankTransferPayment(String accountNumber, String routingNumber) {
        this.accountNumber = accountNumber;
        this.routingNumber = routingNumber;
    }

    @Override
    public void pay(double amount) {
        System.out.println(amount + " paid via bank transfer to account " + accountNumber);
    }
}

// Context
public class PaymentContext {
    private PaymentStrategy paymentStrategy;

    public PaymentContext(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void setPaymentStrategy(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void executePayment(double amount) {
        paymentStrategy.pay(amount);
    }
}
```

**Użycie:**

```java
public class PaymentExample {
    public static void main(String[] args) {
        PaymentContext context = new PaymentContext(
            new CreditCardPayment("John Doe", "1234-5678-9012-3456", "123", "12/25")
        );
        context.executePayment(100.0);

        context.setPaymentStrategy(new PayPalPayment("john@example.com", "password123"));
        context.executePayment(200.0);

        context.setPaymentStrategy(new BankTransferPayment("9876543210", "123456789"));
        context.executePayment(300.0);
    }
}
```

### 4.4 Facade Pattern

**Definicja:** Zapewnia uproszczony interface do złożonego subsystemu.

```java
// Complex subsystem classes
public class CPU {
    public void processData() {
        System.out.println("CPU is processing data...");
    }

    public void freeze() {
        System.out.println("CPU frozen");
    }

    public void jump(long position) {
        System.out.println("CPU jumping to position " + position);
    }

    public void execute() {
        System.out.println("CPU executing instructions");
    }
}

public class Memory {
    public void load(long position, byte[] data) {
        System.out.println("Memory loading data from position " + position);
    }

    public void free(long position) {
        System.out.println("Memory freed at position " + position);
    }
}

public class HardDrive {
    public byte[] read(long lba, int size) {
        System.out.println("HardDrive reading " + size + " bytes from LBA " + lba);
        return new byte[size];
    }

    public void write(long lba, byte[] data) {
        System.out.println("HardDrive writing data to LBA " + lba);
    }
}

// Facade class
public class ComputerFacade {
    private CPU cpu;
    private Memory memory;
    private HardDrive hardDrive;

    private static final long BOOT_ADDRESS = 0;
    private static final long BOOT_SECTOR = 0;
    private static final int SECTOR_SIZE = 512;

    public ComputerFacade() {
        cpu = new CPU();
        memory = new Memory();
        hardDrive = new HardDrive();
    }

    public void start() {
        System.out.println("Starting computer...");
        cpu.freeze();
        memory.load(BOOT_ADDRESS, hardDrive.read(BOOT_SECTOR, SECTOR_SIZE));
        cpu.jump(BOOT_ADDRESS);
        cpu.execute();
        System.out.println("Computer has started successfully!");
    }

    public void shutdown() {
        System.out.println("Shutting down computer...");
        // Complex shutdown sequence
        System.out.println("Computer shut down successfully!");
    }
}
```

**Użycie:**

```java
public class ComputerExample {
    public static void main(String[] args) {
        ComputerFacade computer = new ComputerFacade();
        computer.start();    // Simple interface hides complexity
        computer.shutdown(); // Client doesn't need to know internal details
    }
}
```

### 4.5 Dependency Injection

**Definicja:** Design pattern gdzie dependencies są dostarczane do obiektu zamiast być przez niego tworzone.

#### Constructor Injection (Recommended)

```java
public class OrderService {
    private final PaymentService paymentService;
    private final InventoryService inventoryService;
    private final EmailService emailService;

    public OrderService(PaymentService paymentService,
                       InventoryService inventoryService,
                       EmailService emailService) {
        this.paymentService = paymentService;
        this.inventoryService = inventoryService;
        this.emailService = emailService;
    }

    public void processOrder(Order order) {
        if (inventoryService.isAvailable(order.getProductId())) {
            paymentService.processPayment(order.getAmount());
            emailService.sendConfirmation(order.getCustomerEmail());
        }
    }
}
```

#### Setter Injection

```java
public class OrderService {
    private PaymentService paymentService;
    private InventoryService inventoryService;

    public void setPaymentService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    public void setInventoryService(InventoryService inventoryService) {
        this.inventoryService = inventoryService;
    }
}
```

#### Interface Injection

```java
public interface PaymentServiceInjector {
    void injectPaymentService(PaymentService paymentService);
}

public class OrderService implements PaymentServiceInjector {
    private PaymentService paymentService;

    @Override
    public void injectPaymentService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }
}
```

**Korzyści:**

- Loose coupling
- Testability (mock injection)
- Flexibility
- Single Responsibility Principle

---

## 5. Spring Framework

### 5.1 Spring Bean Scopes

Spring oferuje różne scopes dla beans, kontrolując cykl życia i dostępność instancji.

#### singleton (Default)

Jedna instancja na Spring Container.

```java
@Component
@Scope("singleton") // lub @Scope(ConfigurableBeanFactory.SCOPE_SINGLETON)
public class SingletonBean {
    // Same instance shared across application
}
```

#### prototype

Nowa instancja przy każdym żądaniu.

```java
@Component
@Scope("prototype")
public class PrototypeBean {
    // New instance every time
}
```

#### request (Web)

Jedna instancja na HTTP request.

```java
@Component
@Scope("request")
public class RequestScopedBean {
    // New instance per HTTP request
}
```

#### session (Web)

Jedna instancja na HTTP session.

```java
@Component
@Scope("session")
public class SessionScopedBean {
    // New instance per HTTP session
}
```

#### application (Web)

Jedna instancja na ServletContext.

```java
@Component
@Scope("application")
public class ApplicationScopedBean {
    // One instance per ServletContext
}
```

#### websocket (Web)

Jedna instancja na WebSocket session.

```java
@Component
@Scope("websocket")
public class WebSocketScopedBean {
    // One instance per WebSocket session
}
```

### 5.2 Spring Bean Lifecycle

Pełny cykl życia Spring Bean:

1. **Container Started**
2. **Bean Instantiation** - Spring tworzy instancję
3. **Dependencies Injection** - Wstrzykiwanie dependencies
4. **BeanNameAware.setBeanName()** - Jeśli bean implementuje BeanNameAware
5. **BeanFactoryAware.setBeanFactory()** - Jeśli implementuje BeanFactoryAware
6. **ApplicationContextAware.setApplicationContext()** - Jeśli implementuje ApplicationContextAware
7. **@PostConstruct / InitializingBean.afterPropertiesSet()** - Inicjalizacja
8. **Custom init method** - Metoda określona w @Bean(initMethod)
9. **Bean Ready for Use**
10. **@PreDestroy / DisposableBean.destroy()** - Przed zniszczeniem
11. **Custom destroy method** - Metoda określona w @Bean(destroyMethod)

```java
@Component
public class LifecycleBean implements BeanNameAware, BeanFactoryAware,
                                    ApplicationContextAware, InitializingBean, DisposableBean {

    @Override
    public void setBeanName(String name) {
        System.out.println("1. setBeanName: " + name);
    }

    @Override
    public void setBeanFactory(BeanFactory beanFactory) throws BeansException {
        System.out.println("2. setBeanFactory");
    }

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        System.out.println("3. setApplicationContext");
    }

    @PostConstruct
    public void postConstruct() {
        System.out.println("4. @PostConstruct");
    }

    @Override
    public void afterPropertiesSet() throws Exception {
        System.out.println("5. afterPropertiesSet");
    }

    @PreDestroy
    public void preDestroy() {
        System.out.println("6. @PreDestroy");
    }

    @Override
    public void destroy() throws Exception {
        System.out.println("7. destroy");
    }
}
```

### 5.3 @Qualifier Annotation

**Definicja:** Używane do rozwiązywania niejednoznaczności gdy wiele beans tego samego typu istnieje.

```java
// Multiple implementations
@Component
@Qualifier("email")
public class EmailNotificationService implements NotificationService {
    @Override
    public void sendNotification(String message) {
        System.out.println("Email: " + message);
    }
}

@Component
@Qualifier("sms")
public class SmsNotificationService implements NotificationService {
    @Override
    public void sendNotification(String message) {
        System.out.println("SMS: " + message);
    }
}

// Usage
@Service
public class UserService {
    private final NotificationService emailService;
    private final NotificationService smsService;

    public UserService(@Qualifier("email") NotificationService emailService,
                      @Qualifier("sms") NotificationService smsService) {
        this.emailService = emailService;
        this.smsService = smsService;
    }
}
```

### 5.4 @ConditionalOnMissingBean

**Definicja:** Spring Boot annotation która tworzy bean tylko jeśli bean o tym typie/nazwie nie istnieje.

```java
@Configuration
public class AutoConfiguration {

    @Bean
    @ConditionalOnMissingBean
    public DataSource dataSource() {
        // Tworzy domyślny DataSource tylko jeśli nie ma innego
        return new HikariDataSource();
    }

    @Bean
    @ConditionalOnMissingBean(name = "customService")
    public MyService myService() {
        return new DefaultMyService();
    }
}
```

**Przypadki użycia:**

- Auto-configuration w Spring Boot
- Domyślne implementacje
- Biblioteki zapewniające fallback beans

### 5.5 Time Scheduling w Spring Boot

Spring Boot oferuje wbudowane wsparcie dla task scheduling.

```java
@SpringBootApplication
@EnableScheduling
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

@Component
public class ScheduledTasks {

    // Fixed rate - co 5 sekund
    @Scheduled(fixedRate = 5000)
    public void reportCurrentTime() {
        System.out.println("Current time: " + new Date());
    }

    // Fixed delay - 5 sekund po zakończeniu poprzedniego
    @Scheduled(fixedDelay = 5000)
    public void doSomethingWithDelay() {
        System.out.println("Fixed delay task: " + new Date());
    }

    // Cron expression - codziennie o 9:00
    @Scheduled(cron = "0 0 9 * * ?")
    public void dailyTask() {
        System.out.println("Daily task executed at 9 AM");
    }

    // Cron z timezone
    @Scheduled(cron = "0 0 12 * * ?", zone = "Europe/Warsaw")
    public void lunchTimeTask() {
        System.out.println("Lunch time in Warsaw!");
    }
}
```

**Cron Expression Format:**

```
┌───────────── second (0-59)
│ ┌───────────── minute (0-59)
│ │ ┌───────────── hour (0-23)
│ │ │ ┌───────────── day of month (1-31)
│ │ │ │ ┌───────────── month (1-12 or JAN-DEC)
│ │ │ │ │ ┌───────────── day of week (0-7 or SUN-SAT)
│ │ │ │ │ │
* * * * * *
```

**Przykłady Cron:**

- `0 0 * * * *` - co godzinę
- `0 */15 * * * *` - co 15 minut
- `0 0 8-10 * * *` - codziennie o 8, 9 i 10
- `0 0/30 8-10 * * *` - co 30 minut między 8-10
- `0 0 9-17 * * MON-FRI` - co godzinę, pon-pt, 9-17

### 5.6 Spring Transaction Management

#### @Transactional Annotation

```java
@Service
@Transactional
public class UserService {

    @Transactional(readOnly = true)
    public User findUser(Long id) {
        return userRepository.findById(id);
    }

    @Transactional(
        isolation = Isolation.READ_COMMITTED,
        propagation = Propagation.REQUIRED,
        timeout = 30,
        rollbackFor = {BusinessException.class},
        noRollbackFor = {MinorException.class}
    )
    public void createUser(User user) {
        userRepository.save(user);
        auditService.logUserCreation(user); // Część tej samej transakcji
    }
}
```

#### Transaction Propagation

**REQUIRED (Default):** Dołącza do istniejącej transakcji lub tworzy nową.

```java
@Transactional(propagation = Propagation.REQUIRED)
public void methodA() {
    // Jeśli jest transakcja - używa jej, jeśli nie - tworzy nową
}
```

**REQUIRES_NEW:** Zawsze tworzy nową transakcję, zawiesza obecną.

```java
@Transactional(propagation = Propagation.REQUIRES_NEW)
public void methodB() {
    // Zawsze nowa transakcja
}
```

**SUPPORTS:** Używa transakcji jeśli istnieje, nie tworzy nowej.

**NOT_SUPPORTED:** Zawiesza obecną transakcję i wykonuje bez transakcji.

**MANDATORY:** Wymaga istniejącej transakcji, rzuca wyjątek jeśli nie ma.

**NEVER:** Rzuca wyjątek jeśli transakcja istnieje.

**NESTED:** Tworzy nested transaction (savepoint).

---

## 6. Współbieżność i Threading

### 6.1 Race Condition

**Definicja:** Sytuacja gdzie wynik operacji zależy od timing lub kolejności wykonania wątków.

```java
public class RaceConditionExample {
    private int counter = 0;

    // Niebezpieczna metoda - race condition
    public void increment() {
        counter++; // To NIE jest atomic! (read, increment, write)
    }

    public int getCounter() {
        return counter;
    }
}

// Demonstration
public class RaceConditionDemo {
    public static void main(String[] args) throws InterruptedException {
        RaceConditionExample example = new RaceConditionExample();

        Thread thread1 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) {
                example.increment();
            }
        });

        Thread thread2 = new Thread(() -> {
            for (int i = 0; i < 10000; i++) {
                example.increment();
            }
        });

        thread1.start();
        thread2.start();

        thread1.join();
        thread2.join();

        System.out.println("Final count: " + example.getCounter());
        // Może być mniej niż 20000!
    }
}
```

#### Rozwiązanie - Synchronized

```java
public class ThreadSafeCounter {
    private int counter = 0;

    public synchronized void increment() {
        counter++; // Teraz atomic
    }

    public synchronized int getCounter() {
        return counter;
    }
}
```

#### Rozwiązanie - AtomicInteger

```java
public class AtomicCounter {
    private AtomicInteger counter = new AtomicInteger(0);

    public void increment() {
        counter.incrementAndGet();
    }

    public int getCounter() {
        return counter.get();
    }
}
```

### 6.2 Deadlock

**Definicja:** Sytuacja gdzie dwa lub więcej wątków czekają na siebie nawzajem, blokując się na zawsze.

**Warunki do wystąpienia deadlock:**

1. **Mutual Exclusion** - zasoby nie mogą być współdzielone
2. **Hold and Wait** - proces trzyma zasób i czeka na inny
3. **No Preemption** - zasoby nie mogą być wymusowo odebrane
4. **Circular Wait** - cykliczne oczekiwanie na zasoby

```java
public class DeadlockExample {
    private final Object lock1 = new Object();
    private final Object lock2 = new Object();

    public void method1() {
        synchronized (lock1) {
            System.out.println("Thread 1: Holding lock 1...");

            try { Thread.sleep(100); } catch (InterruptedException e) {}

            synchronized (lock2) {
                System.out.println("Thread 1: Holding lock 1 & 2...");
            }
        }
    }

    public void method2() {
        synchronized (lock2) {
            System.out.println("Thread 2: Holding lock 2...");

            try { Thread.sleep(100); } catch (InterruptedException e) {}

            synchronized (lock1) {
                System.out.println("Thread 2: Holding lock 1 & 2...");
            }
        }
    }
}
```

#### Deadlock Prevention Strategies

**1. Lock Ordering:** Zawsze nabywaj locki w tej samej kolejności

```java
public void safeMethod1() {
    synchronized (lock1) {
        synchronized (lock2) {
            // Work
        }
    }
}

public void safeMethod2() {
    synchronized (lock1) { // Ta sama kolejność!
        synchronized (lock2) {
            // Work
        }
    }
}
```

**2. Timeout:** Użyj tryLock() z timeoutem

```java
public void timeoutMethod() {
    try {
        if (lock1.tryLock(1000, TimeUnit.MILLISECONDS)) {
            try {
                if (lock2.tryLock(1000, TimeUnit.MILLISECONDS)) {
                    try {
                        // Work
                    } finally {
                        lock2.unlock();
                    }
                }
            } finally {
                lock1.unlock();
            }
        }
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
}
```

### 6.3 Optimistic vs Pessimistic Locking

#### Optimistic Locking

**Zakłada:** Konflikty są rzadkie, więc nie blokuj zasobów.
**Mechanizm:** Version field, sprawdź przed zapisem.

```java
@Entity
public class Product {
    @Id
    private Long id;

    private String name;
    private BigDecimal price;

    @Version
    private Long version; // Hibernate automatycznie zarządza

    // getters/setters
}

@Service
public class ProductService {

    @Transactional
    public void updateProduct(Long id, String newName) {
        Product product = productRepository.findById(id);
        product.setName(newName);
        // Hibernate sprawdzi version przy UPDATE
        // Jeśli version się zmieniła, rzuci OptimisticLockException
        productRepository.save(product);
    }
}
```

#### Pessimistic Locking

**Zakłada:** Konflikty są częste, więc zablokuj zasób.
**Mechanizm:** Database locks (SELECT FOR UPDATE).

```java
@Repository
public class ProductRepository {

    @Lock(LockModeType.PESSIMISTIC_WRITE)
    @Query("SELECT p FROM Product p WHERE p.id = :id")
    Product findByIdWithLock(@Param("id") Long id);

    // LockModeType.PESSIMISTIC_READ - shared lock
    // LockModeType.PESSIMISTIC_WRITE - exclusive lock
    // LockModeType.PESSIMISTIC_FORCE_INCREMENT - lock + increment version
}
```

| Cecha             | Optimistic                 | Pessimistic       |
| ----------------- | -------------------------- | ----------------- |
| Performance       | Lepszy (no locking)        | Gorszy (blocking) |
| Scalability       | Lepsza                     | Gorsza            |
| Conflict handling | Retry/rollback             | Prevention        |
| Database load     | Mniejsze                   | Większe           |
| Use case          | Wysokie read, niskie write | Częste konflikty  |

### 6.4 Semaphores

**Definicja:** Mechanizm synchronizacji kontrolujący dostęp do ograniczonej liczby zasobów.

```java
import java.util.concurrent.Semaphore;

public class SemaphoreExample {
    private final Semaphore semaphore;

    public SemaphoreExample(int permits) {
        this.semaphore = new Semaphore(permits);
    }

    public void accessResource() {
        try {
            semaphore.acquire(); // Czeka na dostępne pozwolenie
            System.out.println(Thread.currentThread().getName() + " accessing resource");
            Thread.sleep(2000); // Simulate work
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            semaphore.release(); // Zwalnia pozwolenie
            System.out.println(Thread.currentThread().getName() + " released resource");
        }
    }

    public boolean tryAccessResource(long timeout, TimeUnit unit) {
        try {
            if (semaphore.tryAcquire(timeout, unit)) {
                try {
                    // Do work
                    return true;
                } finally {
                    semaphore.release();
                }
            }
            return false; // Nie udało się uzyskać pozwolenia
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return false;
        }
    }
}

// Przykład użycia - ograniczenie połączeń do bazy danych
public class DatabaseConnectionPool {
    private final Semaphore semaphore = new Semaphore(10); // Max 10 połączeń

    public void executeQuery(String query) {
        try {
            semaphore.acquire();
            // Wykonaj zapytanie do bazy
            System.out.println("Executing: " + query);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            semaphore.release();
        }
    }
}
```

**Przykłady zastosowań:**

- Ograniczenie liczby równoczesnych połączeń do bazy
- Rate limiting
- Resource pooling
- Ograniczenie równoczesnych downloadów

### 6.5 Future, Callable, Runnable, FutureTask

#### Runnable vs Callable

| Cecha        | Runnable                | Callable              |
| ------------ | ----------------------- | --------------------- |
| Method       | run()                   | call()                |
| Return value | void                    | T (generic)           |
| Exception    | Nie może rzucać checked | Może rzucać Exception |
| Wprowadzenie | Java 1.0                | Java 5.0              |

```java
// Runnable - nie zwraca wartości
Runnable task1 = () -> {
    System.out.println("Runnable task executing...");
    // Nie może rzucać checked exceptions
};

// Callable - zwraca wartość
Callable<String> task2 = () -> {
    Thread.sleep(1000); // Może rzucać InterruptedException
    return "Task completed with result";
};
```

#### Future Interface

**Definicja:** Reprezentuje wynik asynchronicznej operacji.

```java
public class FutureExample {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // Submit Callable - zwraca Future
        Future<String> future = executor.submit(() -> {
            Thread.sleep(2000);
            return "Hello from Future!";
        });

        // Submit Runnable - zwraca Future<?>
        Future<?> voidFuture = executor.submit(() -> {
            System.out.println("Runnable task");
        });

        // Sprawdź status
        System.out.println("Is done: " + future.isDone());
        System.out.println("Is cancelled: " + future.isCancelled());

        // Pobierz wynik (blocking)
        String result = future.get(); // Czeka na zakończenie
        System.out.println("Result: " + result);

        // Get z timeout
        try {
            String resultWithTimeout = future.get(1, TimeUnit.SECONDS);
        } catch (TimeoutException e) {
            System.out.println("Task didn't complete in time");
        }

        // Cancel task
        boolean cancelled = future.cancel(true); // mayInterruptIfRunning

        executor.shutdown();
    }
}
```

#### FutureTask Class

**Definicja:** Implementacja Future i Runnable, może być uruchamiana bezpośrednio przez Thread.

```java
public class FutureTaskExample {
    public static void main(String[] args) throws Exception {
        // Create FutureTask from Callable
        FutureTask<Integer> futureTask = new FutureTask<>(() -> {
            Thread.sleep(1000);
            return 42;
        });

        // Run in thread
        Thread thread = new Thread(futureTask);
        thread.start();

        // Get result
        Integer result = futureTask.get();
        System.out.println("Result: " + result);

        // Create FutureTask from Runnable + result
        FutureTask<String> futureTask2 = new FutureTask<>(() -> {
            System.out.println("Task executed");
        }, "Success");

        new Thread(futureTask2).start();
        String result2 = futureTask2.get(); // Returns "Success"
    }
}
```

### 6.6 Thread vs Process

| Cecha             | Thread                   | Process                      |
| ----------------- | ------------------------ | ---------------------------- |
| Definition        | Lightweight subprocess   | Independent program instance |
| Memory            | Shared memory space      | Separate memory space        |
| Creation cost     | Low                      | High                         |
| Context switching | Faster                   | Slower                       |
| Communication     | Shared memory            | IPC (pipes, sockets)         |
| Crash impact      | Can crash entire process | Isolated                     |
| Resource sharing  | Share resources          | Own resources                |

```java
// Thread example
public class ThreadExample {
    public static void main(String[] args) {
        Thread thread1 = new Thread(() -> {
            System.out.println("Thread: " + Thread.currentThread().getName());
        });

        Thread thread2 = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("Thread: " + Thread.currentThread().getName());
            }
        });

        thread1.start();
        thread2.start();
    }
}

// Process example
public class ProcessExample {
    public static void main(String[] args) throws Exception {
        // Start new Java process
        ProcessBuilder pb = new ProcessBuilder("java", "-version");
        Process process = pb.start();

        // Read output
        BufferedReader reader = new BufferedReader(
            new InputStreamReader(process.getInputStream())
        );

        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }

        int exitCode = process.waitFor();
        System.out.println("Process finished with exit code: " + exitCode);
    }
}
```

### 6.7 Thread Pools

**Definicja:** Kolekcja pre-initialized threads gotowych do wykonania zadań.

```java
public class ThreadPoolExample {
    public static void main(String[] args) throws Exception {
        // Fixed thread pool
        ExecutorService fixedPool = Executors.newFixedThreadPool(4);

        // Cached thread pool - creates threads as needed
        ExecutorService cachedPool = Executors.newCachedThreadPool();

        // Single thread executor
        ExecutorService singleThread = Executors.newSingleThreadExecutor();

        // Scheduled thread pool
        ScheduledExecutorService scheduledPool = Executors.newScheduledThreadPool(2);

        // Custom ThreadPoolExecutor
        ThreadPoolExecutor customPool = new ThreadPoolExecutor(
            2,                              // corePoolSize
            4,                              // maximumPoolSize
            60L, TimeUnit.SECONDS,          // keepAliveTime
            new LinkedBlockingQueue<>(100), // workQueue
            new ThreadFactory() {
                private int counter = 0;
                @Override
                public Thread newThread(Runnable r) {
                    return new Thread(r, "CustomThread-" + (++counter));
                }
            },
            new ThreadPoolExecutor.CallerRunsPolicy() // RejectedExecutionHandler
        );

        // Submit tasks
        for (int i = 0; i < 10; i++) {
            final int taskNum = i;
            fixedPool.submit(() -> {
                System.out.println("Task " + taskNum + " executed by " +
                    Thread.currentThread().getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // Scheduled task
        scheduledPool.schedule(() -> {
            System.out.println("Delayed task executed");
        }, 2, TimeUnit.SECONDS);

        // Periodic task
        scheduledPool.scheduleAtFixedRate(() -> {
            System.out.println("Periodic task: " + new Date());
        }, 0, 1, TimeUnit.SECONDS);

        // Shutdown
        fixedPool.shutdown();
        if (!fixedPool.awaitTermination(60, TimeUnit.SECONDS)) {
            fixedPool.shutdownNow();
        }
    }
}
```

**Thread Pool Parameters:**

- **corePoolSize:** Minimalna liczba threads
- **maximumPoolSize:** Maksymalna liczba threads
- **keepAliveTime:** Czas życia nadmiarowych threads
- **workQueue:** Kolejka zadań
- **threadFactory:** Factory do tworzenia threads
- **rejectedExecutionHandler:** Handler dla odrzuconych zadań

---

## 7. JPA i Hibernate

### 7.1 Fetch Types: LAZY vs EAGER

#### LAZY Loading

**Definicja:** Dane są ładowane dopiero gdy są potrzebne (przy pierwszym dostępie).

```java
@Entity
public class User {
    @Id
    private Long id;
    private String name;

    @OneToMany(mappedBy = "user", fetch = FetchType.LAZY) // Domyślne dla @OneToMany
    private List<Order> orders;

    @ManyToOne(fetch = FetchType.LAZY) // Domyślne dla @ManyToOne w Hibernate
    private Department department;
}

// Użycie
User user = userRepository.findById(1L);
System.out.println(user.getName()); // OK
// user.getOrders().size(); // LazyInitializationException jeśli sesja zamknięta!
```

#### EAGER Loading

**Definicja:** Dane są ładowane natychmiast wraz z głównym entity.

```java
@Entity
public class User {
    @Id
    private Long id;
    private String name;

    @OneToMany(mappedBy = "user", fetch = FetchType.EAGER)
    private List<Order> orders; // Zawsze ładowane

    @ManyToOne(fetch = FetchType.EAGER)
    private Department department; // Zawsze ładowane
}
```

**Domyślne FetchType:**

- `@OneToOne`: EAGER
- `@ManyToOne`: EAGER (JPA spec), LAZY (Hibernate default)
- `@OneToMany`: LAZY
- `@ManyToMany`: LAZY

#### Rozwiązywanie LazyInitializationException

**1. Open Session in View (Anti-pattern)**

```java
@Transactional
public void processUser() {
    User user = userRepository.findById(1L);
    user.getOrders().forEach(order -> {
        // Process order - sesja nadal otwarta
    });
}
```

**2. JOIN FETCH**

```java
@Query("SELECT u FROM User u JOIN FETCH u.orders WHERE u.id = :id")
User findUserWithOrders(@Param("id") Long id);
```

**3. Entity Graph**

```java
@EntityGraph(attributePaths = {"orders", "department"})
@Query("SELECT u FROM User u WHERE u.id = :id")
User findUserWithGraph(@Param("id") Long id);
```

### 7.2 N+1 Problem

**Problem:** Wykonywanie 1 zapytania głównego + N zapytań dla każdego powiązanego obiektu.

```java
// N+1 Problem example
List<User> users = userRepository.findAll(); // 1 zapytanie
for (User user : users) {
    System.out.println(user.getDepartment().getName()); // N zapytań!
}
```

**Rozwiązania:**

#### 1. JOIN FETCH

```java
@Query("SELECT u FROM User u JOIN FETCH u.department")
List<User> findAllWithDepartment();
```

#### 2. Entity Graph

```java
@EntityGraph(attributePaths = {"department"})
@Query("SELECT u FROM User u")
List<User> findAllWithDepartmentGraph();

// Named Entity Graph
@Entity
@NamedEntityGraph(
    name = "User.withDepartment",
    attributeNodes = @NamedAttributeNode("department")
)
public class User {
    // ...
}

@EntityGraph("User.withDepartment")
List<User> findAll();
```

#### 3. Batch Fetching

```java
@Entity
public class User {
    @ManyToOne(fetch = FetchType.LAZY)
    @BatchSize(size = 10) // Ładuje po 10 departments naraz
    private Department department;
}
```

#### 4. Projection/DTO

```java
public interface UserProjection {
    String getName();
    String getDepartmentName();
}

@Query("SELECT u.name as name, d.name as departmentName " +
       "FROM User u JOIN u.department d")
List<UserProjection> findAllUserProjections();
```

### 7.3 Sequence vs Identity

#### IDENTITY Strategy

**Definicja:** Baza danych generuje klucz (AUTO_INCREMENT w MySQL).

```java
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
}
```

**Charakterystyka:**

- Klucz generowany po INSERT
- Wymaga natychmiastowego INSERT do bazy
- Problemy z batch inserting
- Popularne w MySQL

#### SEQUENCE Strategy

**Definicja:** Używa sekwencji bazodanowej do generowania kluczy.

```java
@Entity
@SequenceGenerator(
    name = "user_seq_gen",
    sequenceName = "user_sequence",
    allocationSize = 50
)
public class User {
    @Id
    @GeneratedValue(
        strategy = GenerationType.SEQUENCE,
        generator = "user_seq_gen"
    )
    private Long id;
}
```

**Charakterystyka:**

- Klucz generowany przed INSERT
- Lepsze performance (allocationSize)
- Obsługuje batch inserting
- Popularne w PostgreSQL, Oracle

| Cecha            | IDENTITY          | SEQUENCE           |
| ---------------- | ----------------- | ------------------ |
| Performance      | Gorsze            | Lepsze             |
| Batch INSERT     | Nie obsługuje     | Obsługuje          |
| Immediate INSERT | Wymagane          | Nie wymagane       |
| Database support | MySQL, SQL Server | PostgreSQL, Oracle |

### 7.4 Hibernate First-Level Cache

**Definicja:** Session-level cache automatycznie zarządzany przez Hibernate.

```java
@Service
@Transactional
public class UserService {

    public void demonstrateFirstLevelCache() {
        // Pierwsza operacja - zapytanie do bazy
        User user1 = entityManager.find(User.class, 1L);

        // Druga operacja - z cache (no SQL query)
        User user2 = entityManager.find(User.class, 1L);

        System.out.println(user1 == user2); // true - ten sam obiekt!

        // Update - tylko zmienia obiekt w cache
        user1.setName("New Name");

        // Flush - wysyła zmiany do bazy
        entityManager.flush();

        // Clear - czyści first-level cache
        entityManager.clear();

        // Teraz nowe zapytanie do bazy
        User user3 = entityManager.find(User.class, 1L);
        System.out.println(user1 == user3); // false - różne obiekty
    }
}
```

**Właściwości:**

- Włączony zawsze (nie można wyłączyć)
- Scope: Hibernate Session/JPA EntityManager
- Automatyczne cache invalidation
- Zapewnia object identity
- Zapobiega duplicate queries w sesji

### 7.5 JPA Entity Lifecycle

**Stany entities:**

#### 1. Transient (New)

Entity nie jest zarządzane przez persistence context.

```java
User user = new User("John"); // Transient state
```

#### 2. Managed (Persistent)

Entity jest zarządzane przez persistence context.

```java
entityManager.persist(user); // Now managed
user.setName("Jane"); // Change will be detected and saved
```

#### 3. Detached

Entity było managed, ale persistence context został zamknięty.

```java
entityManager.close(); // user is now detached
user.setName("Bob"); // Changes won't be saved automatically
```

#### 4. Removed

Entity jest oznaczone do usunięcia.

```java
entityManager.remove(user); // Removed state
// Will be deleted from database on flush/commit
```

**Operacje przejść:**

```java
// Transient -> Managed
entityManager.persist(entity);

// Detached -> Managed
Entity merged = entityManager.merge(entity);

// Managed -> Removed
entityManager.remove(entity);

// Managed -> Detached
entityManager.detach(entity);

// Any -> Transient (after remove + flush)
entityManager.remove(entity);
entityManager.flush();
```

### 7.6 Dirty Checking

**Definicja:** Mechanizm automatycznego wykrywania zmian w managed entities.

```java
@Transactional
public void updateUser(Long id) {
    User user = entityManager.find(User.class, id); // Managed state

    user.setName("New Name"); // Dirty checking tracks this change
    user.setEmail("new@email.com"); // And this change

    // No explicit save needed!
    // Changes automatically saved on transaction commit
}
```

**Jak działa:**

1. Hibernate tworzy snapshot entity przy ładowaniu
2. Przed flush porównuje current state vs snapshot
3. Generuje UPDATE dla zmienionych pól
4. Wykonuje UPDATE podczas flush

**Optimalizacje:**

```java
@Entity
@DynamicUpdate // UPDATE tylko zmienione kolumny
@SelectBeforeUpdate // SELECT przed UPDATE jeśli potrzebne
public class User {
    // Hibernate może optimize based on these annotations
}
```

---

## 8. REST API i Protokoły

### 8.1 HTTP Methods: POST vs PUT vs PATCH

| Method | Idempotent | Safe | Purpose                 |
| ------ | ---------- | ---- | ----------------------- |
| GET    | ✓          | ✓    | Retrieve resource       |
| POST   | ✗          | ✗    | Create resource         |
| PUT    | ✓          | ✗    | Create/Replace resource |
| PATCH  | ✗          | ✗    | Partial update          |
| DELETE | ✓          | ✗    | Remove resource         |

#### POST - Create Resource

```java
@PostMapping("/users")
public ResponseEntity<User> createUser(@RequestBody User user) {
    User created = userService.createUser(user);
    return ResponseEntity.status(HttpStatus.CREATED)
        .location(URI.create("/users/" + created.getId()))
        .body(created);
}
```

#### PUT - Create/Replace Resource

```java
@PutMapping("/users/{id}")
public ResponseEntity<User> replaceUser(@PathVariable Long id, @RequestBody User user) {
    user.setId(id);
    User replaced = userService.replaceUser(user);
    return ResponseEntity.ok(replaced);
}
```

#### PATCH - Partial Update

```java
@PatchMapping("/users/{id}")
public ResponseEntity<User> updateUser(@PathVariable Long id,
                                      @RequestBody Map<String, Object> updates) {
    User updated = userService.partialUpdate(id, updates);
    return ResponseEntity.ok(updated);
}

// JSON Patch example
@PatchMapping(value = "/users/{id}", consumes = "application/json-patch+json")
public ResponseEntity<User> patchUser(@PathVariable Long id,
                                     @RequestBody JsonPatch patch) {
    User user = userService.findById(id);
    JsonNode patched = patch.apply(objectMapper.valueToTree(user));
    User updated = objectMapper.treeToValue(patched, User.class);
    return ResponseEntity.ok(userService.save(updated));
}
```

### 8.2 RESTful API Design Principles

**Cechy RESTful API:**

1. **Stateless:** Każdy request zawiera wszystkie potrzebne informacje
2. **Uniform Interface:** Consistent naming conventions
3. **Resource-based:** URLs reprezentują resources, nie actions
4. **HTTP Methods:** Proper use of GET, POST, PUT, DELETE, PATCH
5. **Status Codes:** Meaningful HTTP status codes
6. **HATEOAS:** Hypermedia as the Engine of Application State

```java
// Good RESTful design
@RestController
@RequestMapping("/api/v1")
public class BookController {

    @GetMapping("/books")                    // GET /api/v1/books
    public List<Book> getAllBooks() { ... }

    @GetMapping("/books/{id}")              // GET /api/v1/books/123
    public Book getBook(@PathVariable Long id) { ... }

    @PostMapping("/books")                   // POST /api/v1/books
    public Book createBook(@RequestBody Book book) { ... }

    @PutMapping("/books/{id}")              // PUT /api/v1/books/123
    public Book updateBook(@PathVariable Long id, @RequestBody Book book) { ... }

    @DeleteMapping("/books/{id}")           // DELETE /api/v1/books/123
    public void deleteBook(@PathVariable Long id) { ... }

    // Nested resources
    @GetMapping("/books/{bookId}/reviews")  // GET /api/v1/books/123/reviews
    public List<Review> getBookReviews(@PathVariable Long bookId) { ... }
}
```

**HTTP Status Codes:**

- **200 OK:** Successful GET, PUT, PATCH
- **201 Created:** Successful POST
- **204 No Content:** Successful DELETE
- **400 Bad Request:** Invalid request
- **401 Unauthorized:** Authentication required
- **403 Forbidden:** Access denied
- **404 Not Found:** Resource not found
- **409 Conflict:** Resource conflict
- **500 Internal Server Error:** Server error

### 8.3 SOAP vs REST

| Aspect         | SOAP                  | REST                  |
| -------------- | --------------------- | --------------------- |
| Protocol       | Protocol (XML-based)  | Architectural style   |
| Transport      | HTTP, SMTP, TCP, UDP  | Primarily HTTP        |
| Message Format | XML only              | JSON, XML, plain text |
| Standards      | WS-\* standards       | HTTP standards        |
| State          | Can be stateful       | Stateless             |
| Caching        | Limited               | HTTP caching          |
| Performance    | Slower (XML overhead) | Faster                |
| Error Handling | SOAP Faults           | HTTP status codes     |

**SOAP Example:**

```xml
<!-- SOAP Request -->
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <auth:Authentication xmlns:auth="http://example.com/auth">
      <auth:username>john</auth:username>
      <auth:password>secret</auth:password>
    </auth:Authentication>
  </soap:Header>
  <soap:Body>
    <m:GetUser xmlns:m="http://example.com/users">
      <m:UserId>123</m:UserId>
    </m:GetUser>
  </soap:Body>
</soap:Envelope>
```

**REST Example:**

```json
GET /api/users/123 HTTP/1.1
Host: api.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Accept: application/json

Response:
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}
```

### 8.4 Pagination

**Problem:** Zwracanie dużej ilości danych może być niewydajne.

#### Offset-based Pagination

```java
@GetMapping("/users")
public Page<User> getUsers(
    @RequestParam(defaultValue = "0") int page,
    @RequestParam(defaultValue = "20") int size,
    @RequestParam(defaultValue = "id") String sortBy,
    @RequestParam(defaultValue = "ASC") String sortDir
) {
    Sort sort = Sort.by(Sort.Direction.fromString(sortDir), sortBy);
    Pageable pageable = PageRequest.of(page, size, sort);
    return userService.findAll(pageable);
}

// Response
{
  "content": [...],
  "pageable": {
    "sort": { "sorted": true, "by": "id", "ascending": true },
    "pageNumber": 0,
    "pageSize": 20
  },
  "totalElements": 100,
  "totalPages": 5,
  "first": true,
  "last": false,
  "numberOfElements": 20
}
```

#### Cursor-based Pagination

```java
@GetMapping("/users")
public ResponseEntity<List<User>> getUsers(
    @RequestParam(required = false) String cursor,
    @RequestParam(defaultValue = "20") int limit
) {
    List<User> users = userService.findAfterCursor(cursor, limit);

    String nextCursor = users.isEmpty() ? null :
        users.get(users.size() - 1).getId().toString();

    HttpHeaders headers = new HttpHeaders();
    if (nextCursor != null) {
        headers.add("X-Next-Cursor", nextCursor);
    }

    return ResponseEntity.ok().headers(headers).body(users);
}
```

**Porównanie:**
| Type | Pros | Cons |
|------|------|------|
| Offset | Simple, allows jumping | Performance degrades, consistency issues |
| Cursor | Consistent, performant | Complex, no jumping |

---

## 9. Bezpieczeństwo

### 9.1 Authentication vs Authorization

#### Authentication (AuthN)

**Definicja:** Proces weryfikacji tożsamości użytkownika - "Kim jesteś?"

```java
@RestController
public class AuthController {

    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@RequestBody LoginRequest request) {
        // Verify credentials
        if (userService.validateCredentials(request.getUsername(), request.getPassword())) {
            String token = jwtService.generateToken(request.getUsername());
            return ResponseEntity.ok(new AuthResponse(token));
        }
        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build();
    }
}
```

**Metody Authentication:**

- Username/Password
- Multi-factor Authentication (MFA)
- Biometric authentication
- Token-based (JWT, OAuth)
- Certificate-based

#### Authorization (AuthZ)

**Definicja:** Proces określania uprawnień użytkownika - "Co możesz robić?"

```java
@RestController
@RequestMapping("/admin")
public class AdminController {

    @GetMapping("/users")
    @PreAuthorize("hasRole('ADMIN')")
    public List<User> getAllUsers() {
        return userService.findAll();
    }

    @DeleteMapping("/users/{id}")
    @PreAuthorize("hasRole('ADMIN') and #id != authentication.principal.id")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }

    @GetMapping("/reports")
    @PreAuthorize("hasAnyRole('ADMIN', 'MANAGER')")
    public List<Report> getReports() {
        return reportService.findAll();
    }
}
```

**Modele Authorization:**

- Role-based Access Control (RBAC)
- Attribute-based Access Control (ABAC)
- Access Control Lists (ACL)
- Rule-based Access Control

### 9.2 OAuth 2.0

**Definicja:** Framework autoryzacji umożliwiający aplikacjom third-party ograniczony dostęp do user accounts.

**OAuth Flows:**

#### Authorization Code Flow

```java
// 1. Redirect user to authorization server
@GetMapping("/login")
public void login(HttpServletResponse response) {
    String authUrl = "https://auth.server.com/oauth/authorize" +
        "?client_id=your_client_id" +
        "&response_type=code" +
        "&scope=read write" +
        "&redirect_uri=http://yourapp.com/callback";
    response.sendRedirect(authUrl);
}

// 2. Handle callback with authorization code
@GetMapping("/callback")
public ResponseEntity<String> callback(@RequestParam String code) {
    // Exchange code for access token
    String token = oauthService.exchangeCodeForToken(code);
    // Use token to access protected resources
    return ResponseEntity.ok("Login successful");
}
```

#### Client Credentials Flow

```java
@Service
public class ApiService {

    public String callProtectedApi() {
        // Get token using client credentials
        String token = restTemplate.postForObject(
            "https://auth.server.com/oauth/token",
            new TokenRequest("client_credentials", clientId, clientSecret),
            TokenResponse.class
        ).getAccessToken();

        // Use token for API calls
        HttpHeaders headers = new HttpHeaders();
        headers.setBearerAuth(token);

        return restTemplate.exchange(
            "https://api.server.com/data",
            HttpMethod.GET,
            new HttpEntity<>(headers),
            String.class
        ).getBody();
    }
}
```

### 9.3 JWT (JSON Web Token)

**Definicja:** Compact, URL-safe means of representing claims between two parties.

**Struktura JWT:** `header.payload.signature`

```java
@Service
public class JwtService {
    private final String secret = "your-secret-key";
    private final long expiration = 86400000; // 24 hours

    public String generateToken(String username) {
        Date now = new Date();
        Date expiryDate = new Date(now.getTime() + expiration);

        return Jwts.builder()
            .setSubject(username)
            .setIssuedAt(now)
            .setExpiration(expiryDate)
            .claim("role", getUserRole(username))
            .signWith(SignatureAlgorithm.HS512, secret)
            .compact();
    }

    public Claims extractClaims(String token) {
        return Jwts.parser()
            .setSigningKey(secret)
            .parseClaimsJws(token)
            .getBody();
    }

    public boolean validateToken(String token) {
        try {
            extractClaims(token);
            return true;
        } catch (JwtException | IllegalArgumentException e) {
            return false;
        }
    }

    public String extractUsername(String token) {
        return extractClaims(token).getSubject();
    }

    public boolean isTokenExpired(String token) {
        Date expiration = extractClaims(token).getExpiration();
        return expiration.before(new Date());
    }
}
```

**JWT Filter Example:**

```java
@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                   HttpServletResponse response,
                                   FilterChain filterChain) throws ServletException, IOException {
        String authHeader = request.getHeader("Authorization");

        if (authHeader != null && authHeader.startsWith("Bearer ")) {
            String token = authHeader.substring(7);

            if (jwtService.validateToken(token)) {
                String username = jwtService.extractUsername(token);
                UserDetails userDetails = userDetailsService.loadUserByUsername(username);

                UsernamePasswordAuthenticationToken authToken =
                    new UsernamePasswordAuthenticationToken(
                        userDetails, null, userDetails.getAuthorities()
                    );

                SecurityContextHolder.getContext().setAuthentication(authToken);
            }
        }

        filterChain.doFilter(request, response);
    }
}
```

### 9.4 Stateless vs Stateful

#### Stateless Applications

**Definicja:** Aplikacja nie przechowuje informacji o stanie między requestami.

```java
// Stateless service - każdy request jest niezależny
@RestController
public class StatelessController {

    @PostMapping("/calculate")
    public ResponseEntity<CalculationResult> calculate(@RequestBody CalculationRequest request) {
        // Wszystkie dane potrzebne do obliczeń są w request
        int result = request.getA() + request.getB();
        return ResponseEntity.ok(new CalculationResult(result));
    }

    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id,
                                       @RequestHeader("Authorization") String token) {
        // Token zawiera wszystkie informacje o autoryzacji
        if (!jwtService.validateToken(token)) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build();
        }

        User user = userService.findById(id);
        return ResponseEntity.ok(user);
    }
}
```

#### Stateful Applications

**Definicja:** Aplikacja przechowuje informacje o stanie między requestami.

```java
// Stateful service - używa session state
@RestController
public class StatefulController {

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody LoginRequest request,
                                       HttpSession session) {
        if (authService.authenticate(request.getUsername(), request.getPassword())) {
            // Przechowuje stan w sesji
            session.setAttribute("username", request.getUsername());
            session.setAttribute("roles", getUserRoles(request.getUsername()));
            return ResponseEntity.ok("Login successful");
        }
        return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build();
    }

    @GetMapping("/profile")
    public ResponseEntity<User> getProfile(HttpSession session) {
        // Wykorzystuje stan z sesji
        String username = (String) session.getAttribute("username");
        if (username == null) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build();
        }

        User user = userService.findByUsername(username);
        return ResponseEntity.ok(user);
    }
}
```

**Porównanie:**

| Aspect         | Stateless                                 | Stateful                       |
| -------------- | ----------------------------------------- | ------------------------------ |
| Scalability    | Lepsze (horizontal scaling)               | Gorsze (session affinity)      |
| Load balancing | Łatwiejsze                                | Złożone (sticky sessions)      |
| Server memory  | Mniejsze zużycie                          | Większe zużycie                |
| Reliability    | Wyższe (no session loss)                  | Niższe (session can be lost)   |
| Performance    | Może być gorsze (więcej danych w request) | Może być lepsze (cached state) |

---

## 10. Garbage Collection

### 10.1 Jak działa Garbage Collection

**Definicja:** Automatyczny proces zarządzania pamięcią, który odzyskuje pamięć zajmowaną przez obiekty, które nie są już używane.

#### Generational Garbage Collection

JVM dzieli heap na generacje based on object age:

**Young Generation:**

- **Eden Space:** Miejsce gdzie tworzone są nowe obiekty
- **Survivor Spaces (S0, S1):** Obiekty, które przeżyły przynajmniej jeden GC

**Old Generation (Tenured):**

- Długożyjące obiekty, które przeżyły wiele GC cycles

**Metaspace (Java 8+):**

- Class metadata (zastąpił Permanent Generation)

```java
// GC Example
public class GCExample {
    public static void main(String[] args) {
        // Objects created in Eden space
        for (int i = 0; i < 100000; i++) {
            String str = new String("Object " + i); // Eligible for GC after loop
        }

        // Force garbage collection (not recommended in production)
        System.gc();

        // Check memory usage
        Runtime runtime = Runtime.getRuntime();
        long totalMemory = runtime.totalMemory();
        long freeMemory = runtime.freeMemory();
        long usedMemory = totalMemory - freeMemory;

        System.out.println("Used memory: " + usedMemory / (1024 * 1024) + " MB");
    }
}
```

#### GC Process

**Minor GC (Young Generation):**

1. New objects created in Eden
2. When Eden fills up, Minor GC triggers
3. Live objects copied to Survivor space
4. Objects that survive multiple Minor GCs promoted to Old Generation

**Major GC (Old Generation):**

1. Triggered when Old Generation fills up
2. More expensive than Minor GC
3. Can cause "Stop the World" events

### 10.2 Types of Garbage Collectors

#### Serial GC

Single-threaded collector, suitable for small applications.

```bash
java -XX:+UseSerialGC MyApp
```

#### Parallel GC (Default in Java 8)

Multi-threaded collector for throughput.

```bash
java -XX:+UseParallelGC -XX:ParallelGCThreads=4 MyApp
```

#### G1 GC (Default in Java 9+)

Low-latency collector for large heaps.

```bash
java -XX:+UseG1GC -XX:MaxGCPauseMillis=100 MyApp
```

#### ZGC (Java 11+)

Ultra-low latency collector.

```bash
java -XX:+UseZGC MyApp
```

### 10.3 Memory Profiling

#### JVM Options for Monitoring

```bash
# Enable GC logging
java -XX:+PrintGC -XX:+PrintGCDetails -XX:+PrintGCTimeStamps MyApp

# Generate heap dump on OutOfMemoryError
java -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/tmp/heapdump.hprof MyApp

# Set heap size
java -Xms1g -Xmx4g MyApp
```

#### Programmatic Memory Monitoring

```java
import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.lang.management.MemoryUsage;

public class MemoryMonitor {
    public static void printMemoryUsage() {
        MemoryMXBean memoryBean = ManagementFactory.getMemoryMXBean();

        MemoryUsage heapMemory = memoryBean.getHeapMemoryUsage();
        MemoryUsage nonHeapMemory = memoryBean.getNonHeapMemoryUsage();

        System.out.println("Heap Memory:");
        System.out.println("  Used: " + heapMemory.getUsed() / (1024 * 1024) + " MB");
        System.out.println("  Max: " + heapMemory.getMax() / (1024 * 1024) + " MB");

        System.out.println("Non-Heap Memory:");
        System.out.println("  Used: " + nonHeapMemory.getUsed() / (1024 * 1024) + " MB");
        System.out.println("  Max: " + nonHeapMemory.getMax() / (1024 * 1024) + " MB");
    }
}
```

---

## 11. SOLID Principles

### 11.1 Single Responsibility Principle (SRP)

**Definicja:** Klasa powinna mieć tylko jeden powód do zmiany.

```java
// Violation of SRP - klasa robi za dużo
public class User {
    private String name;
    private String email;

    public void save() {
        // Database logic - pierwszy powód do zmiany
        Connection conn = DriverManager.getConnection("...");
        // SQL operations
    }

    public void sendEmail() {
        // Email logic - drugi powód do zmiany
        // SMTP operations
    }
}

// Correct SRP implementation
public class User {
    private String name;
    private String email;
    // Only user data - single responsibility
}

public class UserRepository {
    public void save(User user) {
        // Only database operations
    }
}

public class EmailService {
    public void sendEmail(User user, String message) {
        // Only email operations
    }
}
```

### 11.2 Open/Closed Principle (OCP)

**Definicja:** Klasy powinny być otwarte na rozszerzenia, ale zamknięte na modyfikacje.

```java
// Violation - trzeba modyfikować klasę dla nowych typów
public class DiscountCalculator {
    public double calculateDiscount(String customerType, double amount) {
        if ("REGULAR".equals(customerType)) {
            return amount * 0.1;
        } else if ("PREMIUM".equals(customerType)) {
            return amount * 0.2;
        } else if ("VIP".equals(customerType)) {
            return amount * 0.3;
        }
        return 0;
    }
}

// Correct OCP implementation
public interface DiscountStrategy {
    double calculateDiscount(double amount);
}

public class RegularCustomerDiscount implements DiscountStrategy {
    @Override
    public double calculateDiscount(double amount) {
        return amount * 0.1;
    }
}

public class PremiumCustomerDiscount implements DiscountStrategy {
    @Override
    public double calculateDiscount(double amount) {
        return amount * 0.2;
    }
}

public class DiscountCalculator {
    public double calculateDiscount(DiscountStrategy strategy, double amount) {
        return strategy.calculateDiscount(amount);
    }
}
```

### 11.3 Liskov Substitution Principle (LSP)

**Definicja:** Obiekty klasy bazowej powinny być zastępowalne obiektami klas pochodnych.

```java
// LSP violation - Square changes behavior of Rectangle
public class Rectangle {
    protected int width;
    protected int height;

    public void setWidth(int width) {
        this.width = width;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public int getArea() {
        return width * height;
    }
}

public class Square extends Rectangle {
    @Override
    public void setWidth(int width) {
        this.width = width;
        this.height = width; // Zmienia nieoczekiwanie height!
    }

    @Override
    public void setHeight(int height) {
        this.width = height; // Zmienia nieoczekiwanie width!
        this.height = height;
    }
}

// Test that breaks LSP
public void testRectangle(Rectangle rect) {
    rect.setWidth(5);
    rect.setHeight(10);
    assert rect.getArea() == 50; // Fails for Square!
}
```

**Correct LSP implementation:**

```java
public abstract class Shape {
    public abstract int getArea();
}

public class Rectangle extends Shape {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public int getArea() {
        return width * height;
    }
}

public class Square extends Shape {
    private int side;

    public Square(int side) {
        this.side = side;
    }

    @Override
    public int getArea() {
        return side * side;
    }
}
```

### 11.4 Interface Segregation Principle (ISP)

**Definicja:** Klienty nie powinny być zmuszane do zależenia od interfejsów, których nie używają.

```java
// ISP violation - fat interface
public interface Worker {
    void work();
    void eat();
    void sleep();
}

public class HumanWorker implements Worker {
    @Override
    public void work() {
        System.out.println("Human working");
    }

    @Override
    public void eat() {
        System.out.println("Human eating");
    }

    @Override
    public void sleep() {
        System.out.println("Human sleeping");
    }
}

public class RobotWorker implements Worker {
    @Override
    public void work() {
        System.out.println("Robot working");
    }

    @Override
    public void eat() {
        // Robot doesn't eat! ISP violation
        throw new UnsupportedOperationException();
    }

    @Override
    public void sleep() {
        // Robot doesn't sleep! ISP violation
        throw new UnsupportedOperationException();
    }
}
```

**Correct ISP implementation:**

```java
public interface Workable {
    void work();
}

public interface Eatable {
    void eat();
}

public interface Sleepable {
    void sleep();
}

public class HumanWorker implements Workable, Eatable, Sleepable {
    @Override
    public void work() {
        System.out.println("Human working");
    }

    @Override
    public void eat() {
        System.out.println("Human eating");
    }

    @Override
    public void sleep() {
        System.out.println("Human sleeping");
    }
}

public class RobotWorker implements Workable {
    @Override
    public void work() {
        System.out.println("Robot working");
    }
    // Doesn't implement Eatable or Sleepable - no violation!
}
```

### 11.5 Dependency Inversion Principle (DIP)

**Definicja:** High-level modules nie powinny zależeć od low-level modules. Oba powinny zależeć od abstrakcji.

```java
// DIP violation - high-level depends on low-level
public class EmailService {
    public void sendEmail(String message) {
        // Direct email sending logic
    }
}

public class NotificationService { // High-level module
    private EmailService emailService = new EmailService(); // Depends on concrete class!

    public void sendNotification(String message) {
        emailService.sendEmail(message);
    }
}
```

**Correct DIP implementation:**

```java
// Abstraction
public interface MessageService {
    void sendMessage(String message);
}

// Low-level modules
public class EmailService implements MessageService {
    @Override
    public void sendMessage(String message) {
        System.out.println("Email: " + message);
    }
}

public class SmsService implements MessageService {
    @Override
    public void sendMessage(String message) {
        System.out.println("SMS: " + message);
    }
}

public class SlackService implements MessageService {
    @Override
    public void sendMessage(String message) {
        System.out.println("Slack: " + message);
    }
}

// High-level module depends on abstraction
public class NotificationService {
    private final MessageService messageService;

    public NotificationService(MessageService messageService) {
        this.messageService = messageService; // Depends on interface!
    }

    public void sendNotification(String message) {
        messageService.sendMessage(message);
    }
}

// Usage
public class Application {
    public static void main(String[] args) {
        // Easy to switch implementations
        NotificationService emailNotifier = new NotificationService(new EmailService());
        NotificationService smsNotifier = new NotificationService(new SmsService());

        emailNotifier.sendNotification("Hello via Email");
        smsNotifier.sendNotification("Hello via SMS");
    }
}
```

---

## 12. Database Advanced Topics

### 12.1 PreparedStatement vs CallableStatement

#### PreparedStatement

**Definicja:** Precompiled SQL statement, zapobiega SQL injection, lepsze performance.

```java
public class PreparedStatementExample {
    public User findUserById(Long id) throws SQLException {
        String sql = "SELECT * FROM users WHERE id = ?";

        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setLong(1, id); // Safe parameter binding

            try (ResultSet rs = pstmt.executeQuery()) {
                if (rs.next()) {
                    return new User(
                        rs.getLong("id"),
                        rs.getString("name"),
                        rs.getString("email")
                    );
                }
            }
        }
        return null;
    }

    public void batchInsert(List<User> users) throws SQLException {
        String sql = "INSERT INTO users (name, email) VALUES (?, ?)";

        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            for (User user : users) {
                pstmt.setString(1, user.getName());
                pstmt.setString(2, user.getEmail());
                pstmt.addBatch(); // Add to batch
            }

            int[] results = pstmt.executeBatch(); // Execute all at once
            System.out.println("Inserted " + results.length + " records");
        }
    }
}
```

#### CallableStatement

**Definicja:** Używane do wywołania stored procedures i functions w bazie danych.

```java
public class CallableStatementExample {

    // Call stored procedure with IN parameters
    public void updateUserSalary(Long userId, BigDecimal newSalary) throws SQLException {
        String sql = "{call update_user_salary(?, ?)}";

        try (CallableStatement cstmt = connection.prepareCall(sql)) {
            cstmt.setLong(1, userId);
            cstmt.setBigDecimal(2, newSalary);
            cstmt.execute();
        }
    }

    // Call stored procedure with OUT parameter
    public String getUserFullName(Long userId) throws SQLException {
        String sql = "{call get_user_full_name(?, ?)}";

        try (CallableStatement cstmt = connection.prepareCall(sql)) {
            cstmt.setLong(1, userId); // IN parameter
            cstmt.registerOutParameter(2, Types.VARCHAR); // OUT parameter

            cstmt.execute();

            return cstmt.getString(2); // Get OUT parameter
        }
    }

    // Call function
    public BigDecimal calculateBonus(Long userId, BigDecimal baseSalary) throws SQLException {
        String sql = "{? = call calculate_bonus(?, ?)}";

        try (CallableStatement cstmt = connection.prepareCall(sql)) {
            cstmt.registerOutParameter(1, Types.DECIMAL); // Return value
            cstmt.setLong(2, userId);
            cstmt.setBigDecimal(3, baseSalary);

            cstmt.execute();

            return cstmt.getBigDecimal(1);
        }
    }

    // Call procedure with INOUT parameter
    public void processUserData(UserData userData) throws SQLException {
        String sql = "{call process_user_data(?)}";

        try (CallableStatement cstmt = connection.prepareCall(sql)) {
            cstmt.setString(1, userData.getRawData()); // IN value
            cstmt.registerOutParameter(1, Types.VARCHAR); // OUT registration

            cstmt.execute();

            userData.setProcessedData(cstmt.getString(1)); // Get processed result
        }
    }
}
```

### 12.2 ON DELETE CASCADE

**Definicja:** Automatyczne usuwanie powiązanych rekordów gdy parent record jest usuwany.

```sql
-- Table creation with CASCADE
CREATE TABLE departments (
    id BIGINT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    id BIGINT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id BIGINT,
    FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE CASCADE
);

-- When department is deleted, all employees in that department are also deleted
DELETE FROM departments WHERE id = 1;
-- All employees with department_id = 1 are automatically deleted
```

**JPA/Hibernate Implementation:**

```java
@Entity
public class Department {
    @Id
    private Long id;
    private String name;

    @OneToMany(mappedBy = "department", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Employee> employees = new ArrayList<>();
}

@Entity
public class Employee {
    @Id
    private Long id;
    private String name;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "department_id")
    private Department department;
}

// Usage
@Transactional
public void deleteDepartment(Long departmentId) {
    Department department = departmentRepository.findById(departmentId);
    departmentRepository.delete(department);
    // All employees are automatically deleted due to CASCADE
}
```

**Cascade Types:**

- `ON DELETE CASCADE` - usuwa child records
- `ON DELETE SET NULL` - ustawia foreign key na NULL
- `ON DELETE RESTRICT` - zapobiega usunięciu jeśli istnieją child records
- `ON DELETE SET DEFAULT` - ustawia foreign key na wartość domyślną

---

## 13. Advanced Java Concepts

### 13.1 Reflection

**Definicja:** Możliwość inspekcji i modyfikacji runtime behavior klas, interfejsów, pól i metod.

```java
public class ReflectionExample {
    private String privateField = "Private Value";
    public String publicField = "Public Value";

    private void privateMethod(String param) {
        System.out.println("Private method called with: " + param);
    }

    public void publicMethod() {
        System.out.println("Public method called");
    }

    public static void main(String[] args) throws Exception {
        ReflectionExample obj = new ReflectionExample();
        Class<?> clazz = obj.getClass();

        // Get all fields
        Field[] fields = clazz.getDeclaredFields();
        for (Field field : fields) {
            System.out.println("Field: " + field.getName() + ", Type: " + field.getType());

            // Access private field
            if (field.getName().equals("privateField")) {
                field.setAccessible(true);
                String value = (String) field.get(obj);
                System.out.println("Private field value: " + value);

                // Modify private field
                field.set(obj, "Modified Value");
                System.out.println("Modified private field value: " + field.get(obj));
            }
        }

        // Get all methods
        Method[] methods = clazz.getDeclaredMethods();
        for (Method method : methods) {
            System.out.println("Method: " + method.getName());

            // Call private method
            if (method.getName().equals("privateMethod")) {
                method.setAccessible(true);
                method.invoke(obj, "Reflection Parameter");
            }
        }

        // Create instance using reflection
        Constructor<?> constructor = clazz.getConstructor();
        ReflectionExample newObj = (ReflectionExample) constructor.newInstance();

        // Check annotations
        if (clazz.isAnnotationPresent(Deprecated.class)) {
            System.out.println("Class is deprecated");
        }
    }
}
```

**Praktyczne zastosowania:**

- Frameworks (Spring, Hibernate)
- Serialization/Deserialization
- Testing (mocking private methods)
- Configuration loading
- Plugin architectures

### 13.2 Records w Java (Java 14+)

**Definicja:** Compact syntax dla immutable data classes.

```java
// Traditional class
public class PersonClass {
    private final String name;
    private final int age;

    public PersonClass(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() { return name; }
    public int getAge() { return age; }

    @Override
    public boolean equals(Object obj) {
        // Implementation...
    }

    @Override
    public int hashCode() {
        // Implementation...
    }

    @Override
    public String toString() {
        return "PersonClass{name='" + name + "', age=" + age + "}";
    }
}

// Record equivalent
public record PersonRecord(String name, int age) {
    // Automatically generates:
    // - Constructor
    // - Getters (name(), age())
    // - equals(), hashCode(), toString()

    // Custom constructor with validation
    public PersonRecord {
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
    }

    // Additional methods
    public boolean isAdult() {
        return age >= 18;
    }

    // Static factory method
    public static PersonRecord of(String name, int age) {
        return new PersonRecord(name, age);
    }
}

// Usage
public class RecordExample {
    public static void main(String[] args) {
        PersonRecord person = new PersonRecord("John", 25);

        System.out.println(person.name()); // John
        System.out.println(person.age());  // 25
        System.out.println(person); // PersonRecord[name=John, age=25]

        PersonRecord person2 = new PersonRecord("John", 25);
        System.out.println(person.equals(person2)); // true

        // Deconstruction (Java 17+ preview)
        // if (person instanceof PersonRecord(var name, var age)) {
        //     System.out.println("Name: " + name + ", Age: " + age);
        // }
    }
}
```

### 13.3 Try-with-resources

**Definicja:** Automatic resource management - automatyczne zamykanie resources implementing AutoCloseable.

```java
public class TryWithResourcesExample {

    // Traditional approach - verbose and error-prone
    public String readFileOldWay(String fileName) throws IOException {
        FileReader fileReader = null;
        BufferedReader bufferedReader = null;

        try {
            fileReader = new FileReader(fileName);
            bufferedReader = new BufferedReader(fileReader);
            return bufferedReader.readLine();
        } finally {
            if (bufferedReader != null) {
                try {
                    bufferedReader.close();
                } catch (IOException e) {
                    // Log error
                }
            }
            if (fileReader != null) {
                try {
                    fileReader.close();
                } catch (IOException e) {
                    // Log error
                }
            }
        }
    }

    // Try-with-resources - clean and safe
    public String readFileNewWay(String fileName) throws IOException {
        try (FileReader fileReader = new FileReader(fileName);
             BufferedReader bufferedReader = new BufferedReader(fileReader)) {

            return bufferedReader.readLine();
            // Resources automatically closed, even if exception occurs
        }
    }

    // Multiple resources
    public void copyFile(String source, String destination) throws IOException {
        try (FileInputStream fis = new FileInputStream(source);
             FileOutputStream fos = new FileOutputStream(destination);
             BufferedInputStream bis = new BufferedInputStream(fis);
             BufferedOutputStream bos = new BufferedOutputStream(fos)) {

            byte[] buffer = new byte[8192];
            int bytesRead;
            while ((bytesRead = bis.read(buffer)) != -1) {
                bos.write(buffer, 0, bytesRead);
            }
        }
    }

    // Custom AutoCloseable resource
    public static class DatabaseConnection implements AutoCloseable {
        public DatabaseConnection() {
            System.out.println("Database connection opened");
        }

        public void executeQuery(String sql) {
            System.out.println("Executing: " + sql);
        }

        @Override
        public void close() throws Exception {
            System.out.println("Database connection closed");
        }
    }

    public void useCustomResource() throws Exception {
        try (DatabaseConnection connection = new DatabaseConnection()) {
            connection.executeQuery("SELECT * FROM users");
            // Connection automatically closed
        }
    }
}
```

### 13.4 Collections Framework Deep Dive

#### Collections Utility Class

```java
public class CollectionsExample {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>(Arrays.asList("banana", "apple", "cherry"));

        // Sort
        Collections.sort(list);
        System.out.println("Sorted: " + list);

        // Reverse
        Collections.reverse(list);
        System.out.println("Reversed: " + list);

        // Shuffle
        Collections.shuffle(list);
        System.out.println("Shuffled: " + list);

        // Binary search (requires sorted list)
        Collections.sort(list);
        int index = Collections.binarySearch(list, "banana");
        System.out.println("Index of 'banana': " + index);

        // Min/Max
        System.out.println("Min: " + Collections.min(list));
        System.out.println("Max: " + Collections.max(list));

        // Frequency
        list.addAll(Arrays.asList("apple", "apple"));
        System.out.println("Frequency of 'apple': " + Collections.frequency(list, "apple"));

        // Immutable collections
        List<String> immutableList = Collections.unmodifiableList(list);
        // immutableList.add("new"); // Throws UnsupportedOperationException

        // Synchronized collections
        List<String> syncList = Collections.synchronizedList(new ArrayList<>());

        // Empty collections
        List<String> emptyList = Collections.emptyList();
        Set<String> emptySet = Collections.emptySet();
        Map<String, String> emptyMap = Collections.emptyMap();

        // Singleton collections
        List<String> singletonList = Collections.singletonList("only");
        Set<String> singletonSet = Collections.singleton("only");
    }
}
```

---

## 14. Advanced Patterns and Concepts

### 14.1 CQRS (Command Query Responsibility Segregation)

**Definicja:** Wzorzec architektoniczny separujący operacje odczytu (queries) od operacji zapisu (commands).

```java
// Command Side - Write Operations
public class CreateUserCommand {
    private final String name;
    private final String email;

    public CreateUserCommand(String name, String email) {
        this.name = name;
        this.email = email;
    }

    // getters...
}

@Component
public class UserCommandHandler {
    private final UserRepository userRepository;
    private final EventPublisher eventPublisher;

    public void handle(CreateUserCommand command) {
        User user = new User(command.getName(), command.getEmail());
        userRepository.save(user);

        eventPublisher.publish(new UserCreatedEvent(user.getId(), user.getName()));
    }
}

// Query Side - Read Operations
public class UserQuery {
    private final String email;
    private final String namePattern;

    // constructors, getters...
}

@Component
public class UserQueryHandler {
    private final UserReadRepository userReadRepository;

    public List<UserView> handle(UserQuery query) {
        return userReadRepository.findByEmailOrNamePattern(
            query.getEmail(),
            query.getNamePattern()
        );
    }
}

// Separate Read Model
public class UserView {
    private Long id;
    private String name;
    private String email;
    private LocalDateTime createdAt;
    private int orderCount; // Denormalized data

    // constructors, getters...
}

// Event Handler to update read model
@EventHandler
public class UserProjectionHandler {
    private final UserViewRepository userViewRepository;

    public void on(UserCreatedEvent event) {
        UserView view = new UserView(
            event.getUserId(),
            event.getName(),
            event.getEmail(),
            LocalDateTime.now(),
            0
        );
        userViewRepository.save(view);
    }

    public void on(OrderCreatedEvent event) {
        UserView user = userViewRepository.findByUserId(event.getUserId());
        user.incrementOrderCount();
        userViewRepository.save(user);
    }
}
```

**Korzyści:**

- Optimalne modele dla read/write
- Niezależne skalowanie
- Różne technologie dla read/write
- Event sourcing compatibility

### 14.2 Saga Pattern

**Definicja:** Wzorzec zarządzania długotrwałymi transakcjami w systemach rozproszonych.

#### Orchestration-based Saga

```java
@Component
public class OrderSagaOrchestrator {
    private final PaymentService paymentService;
    private final InventoryService inventoryService;
    private final ShippingService shippingService;

    public void processOrder(OrderCreatedEvent event) {
        SagaTransaction saga = new SagaTransaction(event.getOrderId());

        try {
            // Step 1: Reserve inventory
            ReservationResult reservation = inventoryService.reserveItems(
                event.getOrderId(),
                event.getItems()
            );
            saga.addCompensation(() ->
                inventoryService.releaseReservation(reservation.getReservationId())
            );

            // Step 2: Process payment
            PaymentResult payment = paymentService.processPayment(
                event.getOrderId(),
                event.getAmount()
            );
            saga.addCompensation(() ->
                paymentService.refundPayment(payment.getPaymentId())
            );

            // Step 3: Arrange shipping
            ShippingResult shipping = shippingService.arrangeShipping(
                event.getOrderId(),
                event.getShippingAddress()
            );
            saga.addCompensation(() ->
                shippingService.cancelShipping(shipping.getShippingId())
            );

            // All steps successful
            orderService.completeOrder(event.getOrderId());

        } catch (Exception e) {
            // Compensate all completed steps
            saga.compensate();
            orderService.failOrder(event.getOrderId(), e.getMessage());
        }
    }
}

public class SagaTransaction {
    private final String transactionId;
    private final List<Runnable> compensations = new ArrayList<>();

    public SagaTransaction(String transactionId) {
        this.transactionId = transactionId;
    }

    public void addCompensation(Runnable compensation) {
        compensations.add(0, compensation); // Add at beginning for reverse order
    }

    public void compensate() {
        for (Runnable compensation : compensations) {
            try {
                compensation.run();
            } catch (Exception e) {
                // Log compensation failure
                System.err.println("Compensation failed: " + e.getMessage());
            }
        }
    }
}
```

#### Choreography-based Saga

```java
// Each service handles its part and publishes events
@EventHandler
public class PaymentService {

    public void on(OrderCreatedEvent event) {
        try {
            PaymentResult result = processPayment(event.getOrderId(), event.getAmount());
            eventPublisher.publish(new PaymentProcessedEvent(event.getOrderId(), result));
        } catch (Exception e) {
            eventPublisher.publish(new PaymentFailedEvent(event.getOrderId(), e.getMessage()));
        }
    }

    public void on(OrderCancelledEvent event) {
        // Compensating action
        refundPayment(event.getOrderId());
        eventPublisher.publish(new PaymentRefundedEvent(event.getOrderId()));
    }
}

@EventHandler
public class InventoryService {

    public void on(PaymentProcessedEvent event) {
        try {
            ReservationResult result = reserveItems(event.getOrderId());
            eventPublisher.publish(new InventoryReservedEvent(event.getOrderId(), result));
        } catch (Exception e) {
            eventPublisher.publish(new InventoryReservationFailedEvent(event.getOrderId()));
        }
    }

    public void on(PaymentFailedEvent event) {
        // No action needed - payment failed, so don't reserve inventory
    }
}
```

### 14.3 Circuit Breaker Pattern

**Definicja:** Wzorzec zapobiegający kaskadowym awariom przez "wyłączanie" niepracujących serwisów.

```java
public class CircuitBreaker {
    private enum State { CLOSED, OPEN, HALF_OPEN }

    private State state = State.CLOSED;
    private int failureCount = 0;
    private long lastFailureTime = 0;

    private final int failureThreshold;
    private final long timeout;

    public CircuitBreaker(int failureThreshold, long timeout) {
        this.failureThreshold = failureThreshold;
        this.timeout = timeout;
    }

    public <T> T execute(Supplier<T> operation) throws Exception {
        if (state == State.OPEN) {
            if (System.currentTimeMillis() - lastFailureTime > timeout) {
                state = State.HALF_OPEN;
                failureCount = 0;
            } else {
                throw new CircuitBreakerOpenException("Circuit breaker is OPEN");
            }
        }

        try {
            T result = operation.get();
            onSuccess();
            return result;
        } catch (Exception e) {
            onFailure();
            throw e;
        }
    }

    private void onSuccess() {
        failureCount = 0;
        state = State.CLOSED;
    }

    private void onFailure() {
        failureCount++;
        lastFailureTime = System.currentTimeMillis();

        if (failureCount >= failureThreshold) {
            state = State.OPEN;
        }
    }

    public State getState() {
        return state;
    }
}

// Usage example
@Service
public class ExternalApiService {
    private final CircuitBreaker circuitBreaker = new CircuitBreaker(5, 60000); // 5 failures, 1 minute timeout
    private final RestTemplate restTemplate;

    public String callExternalApi(String endpoint) throws Exception {
        return circuitBreaker.execute(() -> {
            ResponseEntity<String> response = restTemplate.getForEntity(endpoint, String.class);
            if (!response.getStatusCode().is2xxSuccessful()) {
                throw new RuntimeException("API call failed: " + response.getStatusCode());
            }
            return response.getBody();
        });
    }
}
```

### 14.4 Retry Pattern

**Definicja:** Wzorzec automatycznego ponowienia operacji po niepowodzeniu.

```java
public class RetryTemplate {
    private final int maxAttempts;
    private final long delayMillis;
    private final double backoffMultiplier;
    private final Class<? extends Exception>[] retryableExceptions;

    @SafeVarargs
    public RetryTemplate(int maxAttempts, long delayMillis, double backoffMultiplier,
                        Class<? extends Exception>... retryableExceptions) {
        this.maxAttempts = maxAttempts;
        this.delayMillis = delayMillis;
        this.backoffMultiplier = backoffMultiplier;
        this.retryableExceptions = retryableExceptions;
    }

    public <T> T execute(Supplier<T> operation) throws Exception {
        Exception lastException = null;
        long currentDelay = delayMillis;

        for (int attempt = 1; attempt <= maxAttempts; attempt++) {
            try {
                return operation.get();
            } catch (Exception e) {
                lastException = e;

                if (attempt == maxAttempts || !isRetryableException(e)) {
                    throw e;
                }

                System.out.println("Attempt " + attempt + " failed, retrying in " + currentDelay + "ms");

                try {
                    Thread.sleep(currentDelay);
                } catch (InterruptedException ie) {
                    Thread.currentThread().interrupt();
                    throw new RuntimeException("Retry interrupted", ie);
                }

                currentDelay = (long) (currentDelay * backoffMultiplier);
            }
        }

        throw lastException;
    }

    private boolean isRetryableException(Exception e) {
        for (Class<? extends Exception> retryableClass : retryableExceptions) {
            if (retryableClass.isInstance(e)) {
                return true;
            }
        }
        return false;
    }
}

// Usage with annotations (Spring Retry)
@Service
public class DatabaseService {

    @Retryable(
        value = {SQLException.class, DataAccessException.class},
        maxAttempts = 3,
        backoff = @Backoff(delay = 1000, multiplier = 2)
    )
    public User findUserById(Long id) {
        // Database operation that might fail
        return userRepository.findById(id);
    }

    @Recover
    public User recoverFromDatabaseError(SQLException ex, Long id) {
        // Fallback method when all retries fail
        System.err.println("All retries failed for user: " + id);
        return new User(); // Return default user or throw custom exception
    }
}
```

---

## 15. Microservices Patterns

### 15.1 Service Discovery

**Definicja:** Mechanizm automatycznego wykrywania i lokalizowania serwisów w architekturze mikrousług.

```java
// Eureka Client Configuration
@SpringBootApplication
@EnableEurekaClient
public class UserServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(UserServiceApplication.class, args);
    }

    @LoadBalanced
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}

// Service calling another service
@Service
public class OrderService {
    private final RestTemplate restTemplate;
    private final DiscoveryClient discoveryClient;

    public OrderService(RestTemplate restTemplate, DiscoveryClient discoveryClient) {
        this.restTemplate = restTemplate;
        this.discoveryClient = discoveryClient;
    }

    public User getUserById(Long userId) {
        // Using service name instead of hardcoded URL
        return restTemplate.getForObject(
            "http://user-service/api/users/" + userId,
            User.class
        );
    }

    public List<String> getAvailableServices() {
        return discoveryClient.getServices();
    }

    public List<ServiceInstance> getUserServiceInstances() {
        return discoveryClient.getInstances("user-service");
    }
}

// Health check for service registration
@RestController
public class HealthController {

    @GetMapping("/health")
    public Map<String, String> health() {
        Map<String, String> status = new HashMap<>();
        status.put("status", "UP");
        status.put("timestamp", LocalDateTime.now().toString());
        return status;
    }
}
```

### 15.2 Load Balancing

**Definicja:** Rozdzielanie ruchu między dostępne instancje serwisu.

```java
// Custom Load Balancer Rule
@Configuration
public class LoadBalancerConfiguration {

    @Bean
    public IRule ribbonRule() {
        return new WeightedResponseTimeRule(); // or RoundRobinRule(), RandomRule()
    }
}

// Manual load balancing
@Service
public class ManualLoadBalancer {
    private final DiscoveryClient discoveryClient;
    private final AtomicInteger counter = new AtomicInteger(0);

    public ServiceInstance chooseInstance(String serviceId) {
        List<ServiceInstance> instances = discoveryClient.getInstances(serviceId);

        if (instances.isEmpty()) {
            throw new IllegalStateException("No instances available for " + serviceId);
        }

        // Round-robin selection
        int index = counter.getAndIncrement() % instances.size();
        return instances.get(index);
    }

    public <T> T callService(String serviceId, String path, Class<T> responseType) {
        ServiceInstance instance = chooseInstance(serviceId);
        String url = "http://" + instance.getHost() + ":" + instance.getPort() + path;

        RestTemplate restTemplate = new RestTemplate();
        return restTemplate.getForObject(url, responseType);
    }
}

// Feign Client with Load Balancing
@FeignClient(name = "user-service", fallback = UserServiceFallback.class)
public interface UserServiceClient {

    @GetMapping("/api/users/{id}")
    User getUserById(@PathVariable Long id);

    @PostMapping("/api/users")
    User createUser(@RequestBody CreateUserRequest request);
}

@Component
public class UserServiceFallback implements UserServiceClient {

    @Override
    public User getUserById(Long id) {
        return new User(); // Fallback user or throw exception
    }

    @Override
    public User createUser(CreateUserRequest request) {
        throw new ServiceUnavailableException("User service is currently unavailable");
    }
}
```

### 15.3 Event-Driven Architecture

**Definicja:** Architektura oparta na produkcji, wykrywaniu i reagowaniu na events.

```java
// Event classes
public class OrderCreatedEvent {
    private final String orderId;
    private final String customerId;
    private final BigDecimal amount;
    private final LocalDateTime timestamp;

    // constructors, getters...
}

public class PaymentProcessedEvent {
    private final String orderId;
    private final String paymentId;
    private final BigDecimal amount;
    private final LocalDateTime timestamp;

    // constructors, getters...
}

// Event Publisher
@Service
public class EventPublisher {
    private final KafkaTemplate<String, Object> kafkaTemplate;

    public void publishEvent(String topic, Object event) {
        kafkaTemplate.send(topic, event);
    }

    public void publishOrderCreated(OrderCreatedEvent event) {
        publishEvent("order-created", event);
    }
}

// Event Consumers
@Component
public class InventoryEventHandler {

    @KafkaListener(topics = "order-created")
    public void handleOrderCreated(OrderCreatedEvent event) {
        System.out.println("Reserving inventory for order: " + event.getOrderId());

        try {
            inventoryService.reserveItems(event.getOrderId(), event.getItems());

            // Publish success event
            eventPublisher.publishEvent("inventory-reserved",
                new InventoryReservedEvent(event.getOrderId()));
        } catch (Exception e) {
            // Publish failure event
            eventPublisher.publishEvent("inventory-reservation-failed",
                new InventoryReservationFailedEvent(event.getOrderId(), e.getMessage()));
        }
    }
}

@Component
public class NotificationEventHandler {

    @KafkaListener(topics = "order-created")
    public void handleOrderCreated(OrderCreatedEvent event) {
        // Send order confirmation email
        emailService.sendOrderConfirmation(event.getCustomerId(), event.getOrderId());
    }

    @KafkaListener(topics = "payment-processed")
    public void handlePaymentProcessed(PaymentProcessedEvent event) {
        // Send payment receipt
        emailService.sendPaymentReceipt(event.getOrderId(), event.getAmount());
    }
}

// Event Store for Event Sourcing
@Entity
@Table(name = "event_store")
public class EventEntity {
    @Id
    private String id;
    private String aggregateId;
    private String eventType;
    private String eventData;
    private LocalDateTime timestamp;

    // constructors, getters, setters...
}

@Repository
public class EventStore {
    private final EventEntityRepository repository;
    private final ObjectMapper objectMapper;

    public void saveEvent(String aggregateId, Object event) {
        EventEntity entity = new EventEntity();
        entity.setId(UUID.randomUUID().toString());
        entity.setAggregateId(aggregateId);
        entity.setEventType(event.getClass().getSimpleName());
        entity.setEventData(objectMapper.writeValueAsString(event));
        entity.setTimestamp(LocalDateTime.now());

        repository.save(entity);
    }

    public List<Object> getEvents(String aggregateId) {
        List<EventEntity> entities = repository.findByAggregateIdOrderByTimestamp(aggregateId);

        return entities.stream()
            .map(this::deserializeEvent)
            .collect(Collectors.toList());
    }

    private Object deserializeEvent(EventEntity entity) {
        try {
            Class<?> eventClass = Class.forName("com.example.events." + entity.getEventType());
            return objectMapper.readValue(entity.getEventData(), eventClass);
        } catch (Exception e) {
            throw new RuntimeException("Failed to deserialize event", e);
        }
    }
}
```

---

## 16. Kafka and Message Streaming

### 16.1 Kafka Delivery Semantics

#### At Most Once

**Definicja:** Wiadomość może być dostarczona zero lub jeden raz (może być utracona, ale nie zduplikowana).

```java
@Configuration
public class AtMostOnceKafkaConfig {

    @Bean
    public ProducerFactory<String, String> producerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.ACKS_CONFIG, "0"); // Fire and forget
        props.put(ProducerConfig.RETRIES_CONFIG, 0);
        props.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, false);

        return new DefaultKafkaProducerFactory<>(props);
    }

    @Bean
    public ConsumerFactory<String, String> consumerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, true); // Auto commit offsets
        props.put(ConsumerConfig.AUTO_COMMIT_INTERVAL_MS_CONFIG, 1000);

        return new DefaultKafkaConsumerFactory<>(props);
    }
}
```

#### At Least Once

**Definicja:** Wiadomość będzie dostarczona jeden lub więcej razy (może być zduplikowana, ale nie utracona).

```java
@Configuration
public class AtLeastOnceKafkaConfig {

    @Bean
    public ProducerFactory<String, String> producerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.ACKS_CONFIG, "all"); // Wait for all replicas
        props.put(ProducerConfig.RETRIES_CONFIG, Integer.MAX_VALUE);
        props.put(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, 5);
        props.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, true);

        return new DefaultKafkaProducerFactory<>(props);
    }

    @Bean
    public ConsumerFactory<String, String> consumerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, false); // Manual commit

        return new DefaultKafkaConsumerFactory<>(props);
    }
}

// Manual offset management for At Least Once
@Service
public class AtLeastOnceConsumer {

    @KafkaListener(topics = "orders")
    public void consume(ConsumerRecord<String, String> record, Acknowledgment ack) {
        try {
            // Process message
            processOrder(record.value());

            // Manually commit offset only after successful processing
            ack.acknowledge();
        } catch (Exception e) {
            // Don't acknowledge - message will be reprocessed
            System.err.println("Processing failed, message will be retried: " + e.getMessage());
        }
    }
}
```

#### Exactly Once

**Definicja:** Wiadomość będzie dostarczona dokładnie jeden raz (ani utracona, ani zduplikowana).

```java
@Configuration
public class ExactlyOnceKafkaConfig {

    @Bean
    public ProducerFactory<String, String> producerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.ACKS_CONFIG, "all");
        props.put(ProducerConfig.RETRIES_CONFIG, Integer.MAX_VALUE);
        props.put(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, 5);
        props.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, true);
        props.put(ProducerConfig.TRANSACTIONAL_ID_CONFIG, "my-transactional-id");

        return new DefaultKafkaProducerFactory<>(props);
    }

    @Bean
    public ConsumerFactory<String, String> consumerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.ISOLATION_LEVEL_CONFIG, "read_committed");
        props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, false);

        return new DefaultKafkaConsumerFactory<>(props);
    }
}

// Transactional producer
@Service
public class ExactlyOnceProducer {
    private final KafkaTransactionManager transactionManager;
    private final KafkaTemplate<String, String> kafkaTemplate;

    @Transactional
    public void sendMessageExactlyOnce(String topic, String message) {
        kafkaTemplate.send(topic, message);

        // If any part of this transaction fails,
        // the Kafka message send will be rolled back
        updateDatabase(message);
    }
}
```

---

## 17. Podsumowanie najważniejszych tematów

### 17.1 Pytania z prawdziwych rekrutacji

**Najczęściej zadawane pytania na poziomie mid/senior:**

1. **Kontrakt hashCode & equals** - zawsze implementować razem, spójność
2. **HashMap internals** - buckety, kolizje, load factor, Java 8 optimizations
3. **Stream API** - lazy evaluation, terminal vs intermediate operations
4. **Lambda expressions** - functional interfaces, method references
5. **StringBuilder vs StringBuffer** - thread safety, performance
6. **Design patterns** - Strategy, Singleton, Builder (praktyczne użycie)
7. **Hibernate N+1 problem** - JOIN FETCH, Entity Graph, batch fetching
8. **EAGER vs LAZY loading** - domyślne wartości, LazyInitializationException
9. **Java pass by value vs reference** - zawsze pass by value (dla references też)
10. **ArrayList vs LinkedList** - random access vs sequential operations
11. **Reflection** - runtime introspection, frameworks usage
12. **Bean scopes** - singleton, prototype, request, session
13. **synchronized vs volatile** - atomicity vs visibility
14. **Optimistic vs Pessimistic locking** - version fields vs SELECT FOR UPDATE
15. **Records** - immutable data classes, automatic methods
16. **Functional interfaces** - Consumer, Supplier, Function, Predicate
17. **Spring transactions** - @Transactional, propagation, isolation
18. **Comparator vs Comparable** - natural vs custom ordering
19. **HTTP methods** - POST vs PUT vs PATCH, idempotency
20. **SOLID principles** - szczególnie Liskov Substitution

### 17.2 Trendy w rekrutacji Java Developer 2024/2025

Aktualne trendy w rekrutacji Java Developer koncentrują się na praktycznej znajomości Spring Boot, mikrousługach i cloud-native development. Rekruterzy coraz częściej pytają o:

- **Cloud platforms** - AWS, Azure, GCP
- **Container technologies** - Docker, Kubernetes
- **Event-driven architecture** - Kafka, RabbitMQ
- **Testing** - Test-driven development, testowanie integration
- **Security** - OAuth 2.0, JWT, Spring Security
- **Performance** - profiling, monitoring, optimization
- **DevOps knowledge** - CI/CD, monitoring tools

### 17.3 Przygotowanie do rozmowy

**Strategia przygotowania:**

1. **Podstawy Java** - collections, concurrent programming, JVM
2. **Spring ecosystem** - Core, Boot, Data, Security
3. **Database** - SQL, JPA/Hibernate, transaction management
4. **Architecture** - microservices, design patterns, SOLID
5. **Praktyczne zadania** - coding exercises, system design
6. **Behavioral questions** - teamwork, problem solving

**Przykładowe zadania programistyczne:**

- Implementacja LRU Cache
- REST API design i implementacja
- Database schema design
- Microservices communication patterns
- Error handling strategies

To obszerne opracowanie zawiera wszystkie kluczowe tematy z notatek kolegi, rozszerzone o aktualne trendy i praktyczne przykłady. Materiał jest uporządkowany tematycznie i zawiera konkretne implementacje, które mogą być przydatne podczas przygotowania do rozmów rekrutacyjnych na stanowisko Java Developer.
