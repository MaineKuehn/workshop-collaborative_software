# Game of Life

![Game of Life](resources/Gospers_glider_gun.gif)

Johan G. Bonte / [CC-BY-SA-3.0](http://creativecommons.org/licenses/by-sa/3.0/)

--

# The Board

* 2D playing field of *cells*
* Each cell is either dead or alive
* Neighbours preserve, kill or spawn alive cells


	###		o cell
	#o#		# neighbour
	###

--

# The Cells

* 2 Neighbours: Survive
* 3 Neighbours: Spawn or Survive
* `or die`

--

# Your Mission

* Implement Game of Life
	* <!-- .element: class="fragment" --> **Just kidding!**
* <!-- .element: class="fragment" --> `fork` the workshop repository 
* Implement a new feature <!-- .element: class="fragment" -->
	* <!-- .element: class="fragment" --> Random pattern in `gksol.patterns`

--

# Hints

* Use a feature branch for implementation
	* Don't forget about `--no-ff` when merging
* Make use of a `develop` branch
