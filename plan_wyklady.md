
## 📖 Plan wykładu  

### Wprowadzenie (15 min)  
- **Czym jest analiza danych w czasie rzeczywistym?**  
  - Definicja i kluczowe koncepcje  
  - Przykłady zastosowań w biznesie i technologii  
  - Różnice między **real-time analytics, near real-time analytics, batch processing**  
- **Dlaczego real-time analytics jest ważne?**  
  - Przykłady użycia: monitoring systemów IT, analiza IoT, fraud detection, dynamiczne systemy rekomendacyjne  
  - Wyzwania związane z analizą danych w czasie rzeczywistym  

### 2️⃣ Batch vs. Streaming vs. Real-Time Analytics (20 min)  
- **Batch processing**  
  - Czym jest? Kiedy jest stosowany?  
  - Przykłady: tradycyjne raportowanie, analizy historyczne  
- **Streaming analytics (strumieniowe przetwarzanie danych)**  
  - Jak działa? W jakich sytuacjach jest używane?  
  - Przykłady: analiza logów, IoT, detekcja anomalii  
- **Real-time analytics (analityka w czasie rzeczywistym)**  
  - Jakie systemy spełniają kryteria real-time?  
  - Przykłady: systemy rekomendacyjne (**Netflix, Spotify**), dynamiczne ceny (**Uber, Amazon**)  

### 3️⃣ Architektura systemów real-time (20 min)  
- **Kluczowe komponenty**  
  - 📡 Źródła danych: **sensory, API, bazy danych, IoT**  
  - 📩 Systemy kolejkowe: **Apache Kafka, RabbitMQ**  
  - 🖥 Warstwa obliczeniowa: **Apache Flink, Spark Streaming**  
  - 📊 Warstwa analityczna: **ML, systemy detekcji anomalii**  
- **Porównanie podejść Lambda i Kappa**  
  - Kiedy stosować **Lambda Architecture** (batch + stream)?  
  - Kiedy wystarczy **Kappa Architecture** (tylko streaming)?  

### 4️⃣ Wyzwania i problemy analizy danych w czasie rzeczywistym (15 min)  
- ⚡ **Opóźnienia i latencja** – co oznacza "real-time" w różnych kontekstach?  
- 📈 **Obsługa dużych wolumenów danych** – jak efektywnie przetwarzać miliony zdarzeń na sekundę?  
- ⚖ **Dokładność vs. szybkość**

