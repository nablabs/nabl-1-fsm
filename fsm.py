
# This class will take a string as an argument and run a finite state machine on it.
class FiniteStateMachine:
    def __init__(self, fsm: str):
        """
        :param fsm: A string representing a finite state machine. 
        Take this example:
        state start
        state q1
        state q2
        state q3
        transition start a q1
        transition q1 b q2
        transition q2 c q3
        accept q3
        """
        self.fsm = fsm
        self.states = {}
        self.transitions = {}
        self.current_state = None
        self.accepted_states = set()
        self.parse_fsm()

    def parse_fsm(self):
        """
        Parses the finite state machine string and populates the states, transitions and accepted_states attributes.
        """
        for line in self.fsm.splitlines():
            if line.startswith("state"):
                self.parse_state(line)
            elif line.startswith("transition"):
                self.parse_transition(line)
            elif line.startswith("accept"):
                self.parse_accept(line)

    def parse_state(self, line):
        """
        Parses a line that starts with "state" and populates the states attribute.
        """
        _, state = line.split()
        self.states[state] = []

    def parse_transition(self, line):
        """
        Parses a line that starts with "transition" and populates the transitions attribute.
        """
        _, start_state, transition, end_state = line.split()
        self.states[start_state].append((transition, end_state))

    def parse_accept(self, line):
        """
        Sets the accepted states attribute.
        """
        _, state = line.split()
        self.accepted_states.add(state)

    def run(self, string):
        """
        Runs the finite state machine on a string.
        """
        self.current_state = "start"
        for char in string:
            self.current_state = self.get_next_state(self.current_state, char)
        return self.current_state in self.accepted_states

    def get_next_state(self, state, char):
        """
        Gets the next state given the current state and a character.
        """
        for transition, next_state in self.states[state]:
            if transition == char:
                return next_state
        return None