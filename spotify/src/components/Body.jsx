import Dropdown from 'react-bootstrap/Dropdown';

function Body() {
  return (
    <Dropdown>
      <Dropdown.Toggle variant="success" id="dropdown-basic">
        What is your Age
      </Dropdown.Toggle>

      <Dropdown.Menu>
        <Dropdown.Item href="#/action-1">Under 10</Dropdown.Item>
        <Dropdown.Item href="#/action-2">10 - 20</Dropdown.Item>
        <Dropdown.Item href="#/action-3">20+</Dropdown.Item>
      </Dropdown.Menu>
    </Dropdown>
  );
}

export default Body;