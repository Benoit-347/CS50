# ========================= PYTHON METHOD CHEAT SHEET =========================
#  Inside a class, "how the first argument is filled" defines the *kind* of
#  method and its best use-case. Think "who gets auto-injected into arg[0]?".
#
#                                     ┌──────────────────────────────────────┐
#                                     │  BINDING BEHAVIOR (Auto-passed arg)  │
# ┌───────────────────────────────────┴──────────────────────────────────────┴─┐
# │  Normal Method (Instance Method)                             def foo(self) │
# ├────────────────────────────────────────────────────────────────────────────┤
# │ • Defined as:      def method(self, ...)                                   │
# │ • Called as:       obj.method(...)    → Python injects `obj` into arg[0]   │
# │                    Class.method(obj, ...) → you pass obj manually          │
# │                                                                            │
# │ • The function object is a *descriptor*: accessing via instance returns a  │
# │   *bound method* that remembers the instance as "self".                    │
# │ • If you forget `self`, obj.method(...) will still try to pass obj in.     │
# │   → signature mismatch → TypeError. This is why instance methods take self.│
# │ • Use for behavior that *depends on per-object state* (instance attrs).    │
# └────────────────────────────────────────────────────────────────────────────┘
#
# ┌────────────────────────────────────────────────────────────────────────────┐
# │  @classmethod                                            @classmethod      │
# │                                                          def foo(cls)      │
# ├────────────────────────────────────────────────────────────────────────────┤
# │ • Defined as:      @classmethod                                            │
# │                    def method(cls, ...):                                   │
# │ • Called as:       Class.method(...) → Python injects `Class` as `cls`     │
# │                    obj.method(...)   → Python injects type(obj) as `cls`   │
# │                                                                            │
# │ • NOTE: when called on an object, Python is "smart": it passes the *class*,│
# │   not the instance, as first arg. You never see the obj here.              │
# │ • Use when logic belongs to the *type*, not a specific instance:           │
# │     - Alternate constructors (e.g. from_json, from_file, from_db_row)      │
# │     - Polymorphic factories that should honor inheritance:                 │
# │       subclass.from_foo(...) returns a SubClass instance, because `cls`    │
# │       is the subclass, not the base class.                                 │
# │ • Core for inheritance-heavy designs: `cls` lets subclasses customize      │
# │   construction/behavior without rewriting all factory logic.               │
# └────────────────────────────────────────────────────────────────────────────┘
#
# ┌────────────────────────────────────────────────────────────────────────────┐
# │  @staticmethod                                           @staticmethod     │
# │                                                          def foo()         │
# ├────────────────────────────────────────────────────────────────────────────┤
# │ • Defined as:      @staticmethod                                           │
# │                    def method(...):                                        │
# │ • Called as:       Class.method(...) or obj.method(...)                    │
# │                                                                            │
# │ • Python does *not* auto-inject `self` or `cls`. There is no bound method; │
# │   you just get the raw function back.                                      │
# │ • Use for functions that:                                                  │
# │     - Conceptually "live in the class namespace"                           │
# │     - But MUST NOT silently receive an instance or class.                  │
# │ • This is also a *safety fence*:                                           │
# │     - If you defined a normal method but forgot `self`, an instance call   │
# │       would pass `obj` into arg[0] and blow up in weird ways.              │
# │     - Marking it @staticmethod ensures no auto-obj/class is passed;        │
# │       any misuse (wrong arg count) explodes loudly and clearly.            │
# │ • Think of it as "a plain function parked inside the class for             │
# │   namespacing and readability".                                            │
# └────────────────────────────────────────────────────────────────────────────┘
#
# ┌────────────────────────────────────────────────────────────────────────────┐
# │  @property (Data Descriptor - Read Path)                 @property         │
# │                                                          def name(self)    │
# ├────────────────────────────────────────────────────────────────────────────┤
# │ • Defined as:      @property                                               │
# │                    def attr(self):                                         │
# │ • Called as:       obj.attr      # no parentheses!                         │
# │                                                                            │
# │ • When you do `obj.attr`, Python does *not* look directly in obj.__dict__  │
# │   first. It sees the class attribute `attr` is a *data descriptor* (has    │
# │   __get__/__set__), so it calls descriptor.__get__.                        │
# │ • This turns a function into a *computed attribute* — friendlier API:      │
# │     - Public syntax:   obj.width                                           │
# │     - Internal logic:  def width(self): ... compute on the fly ...         │
# │ • Uses:                                                                    │
# │     - Keep existing attribute-style API while changing implementation      │
# │       (e.g., moving from public attr to validation or lazy compute).       │
# │     - Make read-only attributes: just define @property without setter.     │
# │     - Hide invariants behind familiar attribute access.                    │
# └────────────────────────────────────────────────────────────────────────────┘
#
# ┌────────────────────────────────────────────────────────────────────────────┐
# │  @<property>.setter (Data Descriptor - Write Path)       @name.setter      │
# │                                                          def name(self, v) │
# ├────────────────────────────────────────────────────────────────────────────┤
# │ • Defined as:      @attr.setter                                            │
# │                    def attr(self, value):                                  │
# │ • Called as:       obj.attr = value                                        │
# │                                                                            │
# │ • IMPORTANT INTERNAL DETAIL:                                               │
# │     - Python does **not** do a raw `obj.__dict__['attr'] = value` when     │
# │       a data descriptor with __set__ exists.                               │
# │     - Instead, it calls descriptor.__set__(obj, value).                    │
# │     - So "Python does NOT assign obj.attr directly; setter is called".     │
# │ • This allows:                                                             │
# │     - Validation (types, ranges, cross-field invariants)                   │
# │     - Triggering side effects (re-compute caches, notify observers)        │
# │     - Enforcing *write-only* or *restricted* semantics.                    │
# │ • At the class level, accessing `Class.attr` returns the *descriptor* │
# │   object itself, not the value; all magic happens only via instances.      │
# └────────────────────────────────────────────────────────────────────────────┘
#
# ┌────────────────────────────────────────────────────────────────────────────┐
# │  Classes vs Modules vs Plain Functions                                     │
# ├────────────────────────────────────────────────────────────────────────────┤
# │ • A class is both:                                                         │
# │     - A *namespace* (like a dict of functions/attributes), and             │
# │     - A *factory* for instances that carry state.                          │
# │ • You can organize code in several axes:                                   │
# │     - Modules: group by broad feature / program boundary                   │
# │     - Classes: group related behavior + state, inheritance / polymorphism  │
# │     - Plain functions: for simple, stateless transformations               │
# │ • Direct class var access vs @classmethod:                                 │
# │     - Direct: MyClass.x  → "just look this up in the class"                │
# │     - classmethod: cls.x → respects inheritance and allows subclasses to   │
# │       override behavior cleanly. Crucial for reusable hierarchies.         │
# └────────────────────────────────────────────────────────────────────────────┘