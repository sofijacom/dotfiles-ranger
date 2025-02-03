# Import the class
import ranger.gui.context

# Add your key names
ranger.gui.context.CONTEXT_KEYS.append('my_key')

# Set it to False (the default value)
ranger.gui.context.Context.my_key = False

# Or use an array for multiple names
my_keys = ['key_one', 'key_two']
ranger.gui.context.CONTEXT_KEYS.append(my_keys)

# Set them to False
for key in my_keys:
    code = 'ranger.gui.context.Context.' + key + ' = False'
    exec(code)
