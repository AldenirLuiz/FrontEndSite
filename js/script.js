
openMenu.addEventListener('click', () => {

	menu.style.display = "flex"
    menu.style.maxWidth = "100%"

	menu.style.right = (menu.offsetWidth * -1) + 'px'

	setTimeout(()=> {

		menu.style.opacity = '1'
		menu.style.right = "0"
		openMenu.style.display = 'none'
	}, 10);
})

closeMenu.addEventListener('click', () => {

	menu.style.opacity = '0'
	menu.style.right = (menu.offsetWidth * -1) + 'px'

	setTimeout(()=> {
		menu.removeAttribute('style')
		openMenu.removeAttribute('style')
	}, 600);
})

openMore.addEventListener('click', () => {
    p_hide_sobre.style.display = 'block';
    closeMore.style.display = 'flex';
    openMore.style.display = 'none';
})

closeMore.addEventListener('click', () => {
    p_hide_sobre.style.display = 'none';
    closeMore.style.display = 'none';
    openMore.style.display = 'flex';
})