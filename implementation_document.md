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

## **Time and Space Complexities**

### **Trie Construction**
#### **Time Complexity**:
- Let N be the total number of notes in all MIDI files and D the degree of the Markov model.
- Each sequence of D+1 notes requires a traversal or insertion in the trie:
  - **Worst case**: O(N*D)
- Calculating probabilities involves a pass through the trie:
  - **Worst case**: O(N)
- **Overall**: O(N*D)

#### **Space Complexity**:
- The trie stores nodes for unique sequences of length D+1:
  - **Worst case**: O(K*(D+1)), where K is the number of unique notes.

### **Melody Generation**
#### **Time Complexity**:
- Generating M notes requires M trie lookups and random choices:
  - Trie lookups: O(D) per note, or O(M*D) in total.
  - Random selection involves O(L) for L child nodes.
  - **Overall**: O(M*(D + L)).

#### **Space Complexity**:
- The melody sequence requires O(M) storage.

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
