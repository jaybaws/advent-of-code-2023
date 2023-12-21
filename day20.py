from abc import ABC, abstractmethod
from collections import defaultdict, deque
from typing import List, Tuple
from enum import Enum

modules = {}
inputs = {}

class Pulse(Enum):
    HI = "high"
    LO = "low"

class Module(ABC):
    def __init__(self, name: str, connections: List[str]):
        self.name = name
        self.connections = connections
        self.pulse_counts = self.last_signals = defaultdict(lambda : 0)
        self.last_signals = defaultdict(lambda : Pulse.LO)

    def pulses_taken(self) -> (int, int):
        return (self.pulse_counts[Pulse.HI], self.pulse_counts[Pulse.LO])

    def handle(self, p: Pulse, src: str) -> List[Tuple[str, Pulse]]:
        self.pulse_counts[p] += 1
        self.last_signals[src] = p
        return self.do_handle(p, src)

    @abstractmethod
    def do_handle(self, p: Pulse, src: str) -> List[Tuple[str, Pulse]]:
        ...

class BroadCast(Module):
    def do_handle(self, p: Pulse, src: str) -> List[Tuple[str, Pulse]]:
        for c in self.connections:
            yield (c, p)

class FlipFlop(Module):
    def do_handle(self, p: Pulse, src: str) -> List[Tuple[str, Pulse]]:
        if p is Pulse.LO:
            _, lo_taken = self.pulses_taken()
            np = Pulse.HI if lo_taken %2 != 0 else Pulse.LO
            for c in self.connections:
                yield (c, np)

class Conjunction(Module):
    def do_handle(self, p: Pulse, src: str) -> List[Tuple[str, Pulse]]:
        if sum([1 for ins in inputs[self.name] if self.last_signals[ins] is Pulse.LO] ) == 0:
            for c in self.connections:
                yield (c, Pulse.LO)
        else:
            for c in self.connections:
                yield (c, Pulse.HI)

with open("day20_input.txt", "r") as f:
    for name, dests in [ line.split(" -> ") for line in f.read().splitlines() ]:
        dests = dests.split(", ")

        if name.startswith("%"):
            name = name[1:]
            modules[name] = FlipFlop(name, dests)
        elif name.startswith("&"):
            name = name[1:]
            modules[name] = Conjunction(name, dests)
        else:
            modules[name] = BroadCast(name, dests)

        for dest in dests:
            if dest not in inputs:
                inputs[dest] = []
            inputs[dest].append(name)

    for k in [ k for k in inputs.keys() if k not in modules.keys()]:
        modules[k] = BroadCast(k, [])

for attempt in range(1_000):
    q = deque([("broadcaster", Pulse.LO, "button")])
    while q:
        mod_name, p, src_mod_name = q.popleft()
        m: Module = modules[mod_name]
        for dest_name, dest_pulse in m.handle(p, src_mod_name):
            q.append((dest_name, dest_pulse, mod_name))

ans1 = sum([ mod.pulses_taken()[0] for _, mod in modules.items()]) * sum([ mod.pulses_taken()[1] for _, mod in modules.items()])

print(f"ANSWERS -> part1=({ans1}) part2=({None}).")