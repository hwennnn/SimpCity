# SimpCity

## **Links to wiki**

1. [Roadmap](https://github.com/hwennnn/SimpCity/wiki/RoadMap)
2. [Daily Scrum](https://github.com/hwennnn/SimpCity/wiki/Daily-Scrum)
3. [Sprint Goal](https://github.com/hwennnn/SimpCity/wiki/Sprint-Goal)
4. [Sprint Retrospective](https://github.com/hwennnn/SimpCity/wiki/Sprint-Retrospective)
5. [Progress Update Report](https://github.com/hwennnn/SimpCity/wiki/Progress-Report)

## **Development guide**

During development, please create a new branch `feature/{featureName}` from the latest development branch. When the feature is finished developed, please submit a pull request before merging the feature branch to the development branch for code reviewing.

## **Commit messages style**

`<type>: <description>`

- `feat` - adding feature or enhancements to the application
- `fix` - bug fix
- `refactor` - refactoring a specific section of the codebase
- `test` - related to testing
- `docs` - related to documentation
- `ci` - related to continuous integration
- `cd` - related to continuous delivery
- `style` - Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- `chore` - Changes to the build process or auxiliary tools and libraries such as documentation generation

**Notes: Please only specifc one type in one commit!**

## **Pull request template**

**IMPORTANT: Please do not create a Pull Request without creating an issue first.**

_Any change needs to be discussed before proceeding. Failure to do so may result in the rejection of the pull request._

Please provide enough information so that others can review your pull request:

<!-- You can skip this if you're fixing a typo or adding an app to the Showcase. -->

Explain the **details** for making this change. What existing problem does the pull request solve?

<!-- Example: When "Adding a function to do X", explain why it is necessary to have a way to do X. -->

### **Test plan (required)**

Demonstrate the code is solid. Example: The exact commands you ran and their output, screenshots / videos if the pull request changes UI.

### **Closing issues**

Put `Closes #XXXX` in your comment to auto-close the issue that your PR fixes (if such, only put this when the issue is to be completed or else just link the issue).

## **Build with Docker**

### Run docker with -ti flag to run in interative mode

```bash
docker build -t simpcity .
docker run -ti simpcity
```

### Run pytest unit testing in docker

```bash
docker build -t simpcity-test -f Dockerfile.test .
docker run -ti simpcity-test
```

## **Comments Style**

Used to help with generating documentation using pydoc

### Functions

```python

  """
    Summary or Description of the Function should fit in one line

    Parameters:
      argument1 (int): Description of arg1

    Returns:
      int:Returning value

   """

```

### Classes

```python

    """
      Summary line for a class should fit in one line.

      Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

      Properties:
        func1 (int) :  Description of func1

    """
```

## **Credits**

<table>
  <tr>
    <td align="center"><a href="https://github.com/ZacharyHRQ"><img src="https://avatars1.githubusercontent.com/u/25434034?s=460&u=7114f2d5b9704f927adcb4a4c05a7a705f8cbfa6&v=4" width="100px;" alt=""/><br /><sub><b>Zachary Hong Rui Quan <br> (S10185319J) <br>Project Manager</b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/hwennnn"><img src="https://avatars3.githubusercontent.com/u/54523581?s=460&u=a649d3ed6c70ffe2fa69f37c0870415668149113&v=4" width="100px;" alt=""/><br /><sub><b>Wai Hou Man <br> (S10197636F) <br>Tech Lead</b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/NotConfident"><img src="https://avatars.githubusercontent.com/u/52237386?v=4" width="100px;" alt=""/><br /><sub><b>Tee Yong Teng <br> (S10198102E) <br> QA Lead </b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/glennpck"><img src="https://avatars.githubusercontent.com/u/59985863?v=4" width="100px;" alt=""/><br /><sub><b>Glenn Peh Chia Kit <br> (S10195629B) <br> Developer</b></sub></a><br />
    </td>
  </tr>
</table>
