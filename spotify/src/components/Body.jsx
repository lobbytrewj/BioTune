import Dropdown from 'react-bootstrap/Dropdown';

let storedValue = '';

function Body() {
  const meow = () => { 
    storedValue = meow
    console.log(storedValue)
  }
  return (
    <Dropdown>
      <Dropdown.Toggle variant="success" id="dropdown-basic">
        What is your Age
      </Dropdown.Toggle>

      <Dropdown.Menu>
        <Dropdown.Item href="#/action-1" onClick={meow}>Under 10</Dropdown.Item>
        <Dropdown.Item href="#/action-2" onClick={meow}>10 - 20</Dropdown.Item>
        <Dropdown.Item href="#/action-3" onClick={meow}>20+</Dropdown.Item>
      </Dropdown.Menu>
    </Dropdown>
  );
}

export default Body;