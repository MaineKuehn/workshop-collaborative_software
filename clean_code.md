![The only valid measurement of code quality: WTFs/minute](resources/measuring_code_quality.jpg)

--

# Clean Code

* ... is not about formatting style

> Code I'm not afraid to modify

[g andrieu, Stack Overflow](https://stackoverflow.com/questions/954570/definition-of-clean-code)

--

# Clean Code (2)

* Easy to understand
* Easy to modify
* Easy to test
* Does not contain duplicated code
* Works correctly

--

## Code Rotting

* Code gets worse over time
* Code gets worse with number of developers <!-- .element: class="fragment" -->

Instead, every time you look at a piece of code, improve a bit

* Refactoring of names of variables or methods
* Shortening of methods that are too complex/long
* Deduplicate code 
* ...

--

> `assert` No Indico Developer attending the workshop?

--

## What is wrong here?

	from MaKaC.i18n import _

	def _getCheckedIn(self):
	    conf = self._registrant.getConference()
	    if not conf.getRegistrationForm().getETicket().isEnabled():
	        return "-"
	    elif self._registrant.isCheckedIn():
	        return _("Yes")
	    else:
	        return _("No")

--

## What is wrong here? (2)

	def _initStandardPersonalData(self):
	    self._data = PersistentMapping()
	    self._sortedKeys = PersistentList()
	    p = PersonalDataFormItem({'id':'title', 'name': "Title", 'input':'list', 'mandatory':False})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'firstName', 'name': "First Name", 'input':'text', 'mandatory':True})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'surname', 'name': "Surname", 'input':'text', 'mandatory':True})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'position', 'name': "Position", 'input':'text', 'mandatory':False})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'institution', 'name': "Institution", 'input':'text', 'mandatory':True})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'address', 'name': "Address", 'input':'text', 'mandatory':False})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'city', 'name': "City", 'input':'text', 'mandatory':True})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'country', 'name': "Country/Region", 'input':'list', 'mandatory':True})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'phone', 'name': "Phone", 'input':'text', 'mandatory':False})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'fax', 'name': "Fax", 'input':'text', 'mandatory':False})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'email', 'name': "Email", 'input':'hidden', 'mandatory':True})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
	    p = PersonalDataFormItem({'id':'personalHomepage', 'name': "Personal homepage", 'input':'text', 'mandatory':False})
	    self._data[p.getId()] = p
	    self._sortedKeys.append(p.getId())
