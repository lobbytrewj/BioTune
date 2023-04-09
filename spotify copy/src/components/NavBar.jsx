import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Container from 'react-bootstrap/Container';



function Navigation() {
    return (
      <Navbar bg="light" expand="lg" >
        <Container>
          <Navbar.Brand href="#home">MoodTunes</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link as={Link} to ="/">Home</Nav.Link>
              <Nav.Link as={Link} to ="/about">About</Nav.Link>
              <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                <NavDropdown.Item as={Link} to ="/Demo">Demo</NavDropdown.Item>
                <NavDropdown.Item as={Link} to ="/Logic">
                  Logic
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                {/* <NavDropdown.Divider />
                <NavDropdown.Item href="#action/3.4">
                  Separated link
                </NavDropdown.Item> */}
              </NavDropdown>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>




    );
  }
  
  export default Navigation;
