import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Container from 'react-bootstrap/Container';



function Navigation1() {
    return (
        <Navbar bg="light" expand="lg">
          <Container>
            <Navbar.Brand href="#home">MoodTunes</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <Nav.Link href="#home">Home</Nav.Link>
                <Nav.Link href="#link">Options</Nav.Link>
                <NavDropdown title="Song Themes" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.5">
                    Feelings
                    <NavDropdown.Divider />
                  </NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.1">Happy</NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.2">Hype</NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.3">Depressed</NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.4">Relaxation</NavDropdown.Item>
                </NavDropdown>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>  
    );
  }
  
  export default Navigation1;
