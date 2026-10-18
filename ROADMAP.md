# Hand Movement Application — Development Roadmap

## Project Overview

The Hand Movement Application is a computer vision project developed using Python, OpenCV, and MediaPipe.

The project aims to detect and track human hands through a webcam, recognize hand gestures, and explore real-world applications such as gesture-controlled robotics and American Sign Language (ASL) recognition.

The project is being developed incrementally, with an emphasis on understanding the underlying technologies, experimenting with different approaches, and documenting progress.

## Development Milestones

### Milestone 1 — Camera Setup
**Status:** Completed

**Goal:** Establish a functioning webcam capture system using OpenCV.

- [x] Set up Python and OpenCV
- [x] Access laptop webcam
- [x] Capture and display live video
- [x] Record video and save as MP4
- [x] Separate camera setup from image-processing logic

### Milestone 2 — Hand Detection
**Status:** In Progress

**Target Date:** November 1, 2026

**Goal:** Reliably detect hands in a live webcam feed using MediaPipe.

- [ ] Research MediaPipe and understand its capabilities
- [ ] Install and configure MediaPipe
- [ ] Integrate MediaPipe with OpenCV
- [ ] Detect hand presence in individual frames
- [ ] Display 21 hand landmarks
- [ ] Display hand detection status on screen
- [ ] Test detection under different conditions

**Completion criteria:** The application detects whether a hand is visible and displays its landmarks in real time.

### Milestone 3 — Gesture Recognition
**Status:** Not Started

**Target Date:** November 10, 2026

**Goal:** Identify simple hand gestures using detected landmarks.

- [ ] Understand hand landmark coordinates
- [ ] Research MediaPipe Gesture Recognizer
- [ ] Detect an open palm
- [ ] Detect a closed fist
- [ ] Detect pointing and other simple gestures
- [ ] Display recognized gesture labels
- [ ] Improve recognition consistency

**Completion criteria:** The application consistently distinguishes several predefined gestures.

### Milestone 4 — Robot Design & 3D Printing

**Status:** Planned  

**Target Date:** November 30, 2026

**Goal:** Design and fabricate a functional robot chassis using CAD and 3D printing.

**Tasks:**
- [ ] Research robot designs and locomotion systems
- [ ] Choose robot components, including motors, wheels, and controller
- [ ] Measure component dimensions and mounting requirements
- [ ] Create initial CAD design
- [ ] Design motor mounts, chassis, and electronics housing
- [ ] Print prototype components
- [ ] Test component fit and mechanical movement
- [ ] Revise and reprint components as necessary
- [ ] Assemble the mechanical chassis

**Definition of Done:** A mechanically assembled robot chassis with correctly fitted components and mounting points ready for electronics installation.

---

### Milestone 5 — Electronics & Robot Assembly

**Status:** Planned  
**Target Date:** January 1, 2027

**Goal:** Assemble and program the robot's electronics to enable basic movement independently of hand gestures.

**Tasks:**
- [ ] Research motor drivers, power supplies, and microcontrollers
- [ ] Select and purchase required electronic components
- [ ] Create a wiring diagram
- [ ] Connect motors to the motor driver and controller
- [ ] Install the electronics onto the chassis
- [ ] Program basic motor controls
- [ ] Test forward, backward, left, right, and stop movements
- [ ] Test power supply, wiring reliability, and motor performance
- [ ] Troubleshoot hardware and software issues

**Definition of Done:** A fully assembled robot capable of executing basic movement commands independently of the hand-detection application.

---

### Milestone 6 — Gesture-Controlled Robot

**Status:** Planned  
**Target Date:** January 30, 2027

**Goal:** Integrate the Hand Movement Application with the physical robot to enable real-time gesture-based control.

**Tasks:**
- [ ] Design a gesture-to-command mapping
- [ ] Implement command generation using recognized hand gestures
- [ ] Test generated commands without physical hardware
- [ ] Research communication methods (USB, Bluetooth, Wi-Fi)
- [ ] Establish communication between the computer and robot controller
- [ ] Send movement commands from the application to the robot
- [ ] Implement safety stops and communication timeouts
- [ ] Reduce accidental movements caused by incorrect gesture recognition
- [ ] Test gesture detection accuracy and robot responsiveness
- [ ] Demonstrate gesture-controlled robot movement

**Definition of Done:** The robot reliably responds to predefined hand gestures in real time and stops safely when gestures are lost or communication fails.

### Milestone 7 — ASL Recognition

**Status:** Planned

**Goal:** Explore recognition of American Sign Language using computer vision and machine learning.

**Tasks:**
- [ ] Research ASL fingerspelling and recognition approaches 
- [ ] Explore datasets and training requirements
- [ ] Recognize a small set of static ASL letters
- [ ] Build a basic recognition interface
- [ ] Evaluate recognition accuracy
- [ ] Research dynamic signs and continuous sign recognition

A prototype recognizes a selected vocabulary of ASL signs. Full ASL translation remains a separate, more advanced long-term goal.
## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| OpenCV | Webcam capture, image processing, display |
| MediaPipe | Hand landmarks and gesture recognition |
| NumPy | Array and numerical operations |
| Robot hardware | Future physical gesture-control system |

Additional technologies will be introduced as needed.

## Development Approach

- Work on one primary milestone at a time.
- Research and understand unfamiliar technologies before implementation.
- Develop and test features incrementally.
- Document experiments, problems, and solutions in the logbook.
- Review and test changes before merging them into the main branch.
- Prioritize reliable functionality over additional features.

## Future Improvements

- Two-handed gesture recognition
- Custom gesture classification
- More advanced hand movement tracking
- Wireless robot communication
- Real-time gesture feedback
- Expanded ASL vocabulary and dynamic sign recognition

## Project Documentation

Development progress, experiments, and technical challenges are documented in the `logbook/` directory.