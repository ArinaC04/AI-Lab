# **Implementation Document**

## **General Structure of the Program**

### **Note Processing**
- **`note`** and **`midi`**:
  - Convert between MIDI numbers and note representations (e.g., `1 -> C#1`) and vice versa.

### **MIDI File Handling**
- **`midi_to_pitch`**:
  - Extracts note sequences and durations from MIDI files.
- **`pitch_to_midi`**:
  - Converts note sequences back into a MIDI file.

### **Trie Structure for Markov Chain**
- A **trie-based Markov model** is used to store sequences of notes and their probabilities:
  - **`Node` class**:
    - Represents a note, tracks its frequency, child nodes, and stores its probability.
  - **`create_trie`**:
    - Constructs the trie from MIDI files, incorporating sequences up to the user-defined degree.
  - **`get_prob`**:
    - Calculates the probabilities of transitions between nodes in the trie and updates them in the respective nodes.
  - **`print_trie`**:
    - Outputs the trie structure for debugging or analysis.

### **Melody Generation**
- **`generate`**:
  - Uses the trie to create a sequence of notes based on input notes and the specified number of notes to consider.

---
## Time and Space Complexities

### Functions in `functions.py`

#### `create_trie(degree)`
- **Time Complexity**: 
  - `O(n * d)`, where `n` is the total number of notes across all MIDI files, and `d` is the degree.
- **Space Complexity**:
  - `O(k)`, where `k` is the number of unique sequences of `d + 1` notes.

#### `generate(input, n, roots, degree)`
- **Time Complexity**: 
  - `O(n * d)`, where `n` is the number of notes generated and `d` is the degree.
- **Space Complexity**:
  - `O(n)`, for storing the generated melody.

#### `midi_to_pitch(file)`
- **Time Complexity**: 
  - `O(m)`, where `m` is the number of events in the MIDI file.
- **Space Complexity**:
  - `O(p)`, where `p` is the number of unique pitch values.

#### `pitch_to_midi(pitches, duration, instrument)`
- **Time Complexity**: 
  - `O(n)`, where `n` is the number of pitches.
- **Space Complexity**:
  - `O(1)`, as it operates on the MIDI file directly.

### GUI Interactions in `ui.py`

- **Error Handling**: 
  - Time Complexity: `O(1)` for input checks.
  - Space Complexity: `O(1)`.
- **Melody Generation**: Delegates to `functions.py` methods; see their complexities above.

### Overall
- **Time Complexity**: 
  - Melody generation is the dominant factor: `O(n * d)`.
- **Space Complexity**: 
  - Dominated by trie storage: `O(k)`.

### **MIDI Conversion**
#### **Time Complexity**:
- Reading or writing MIDI files iterates through notes:
  - O(M).

#### **Space Complexity**:
- Storage requirements are linear with M:
  - O(M).

---

## **Performance and Big O Analysis Comparison**

### **Trie-Based Markov Model**
#### **Advantages**:
- Efficient prefix-based storage compared to flat transition matrices.
- Allows dynamic probability adjustment with incremental updates.

#### **Drawbacks**:
- Space usage grows exponentially with the degree.

### **Comparison with Alternatives**
- **Transition Matrices**:
  - Better suited for low degrees.
  - Tries are preferable for large data and high degrees due to reduced redundancy.

---

*Note*: I used ChatGPT to assist with understanding concepts such as tries, to troubleshoot setup issues (e.g., Poetry installation) and to format markdown documents. All code was written entirely by me.
