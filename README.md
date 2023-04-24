#  layerd

Mount, Download, and Inspect Lambda Layers in seconds.

> Lambda Layers created by a third party?
>
> Want the contents locally?
>
> Use `layerd`.


# Table of Contents

0. [Inspiration](#inspiration)
1. [Installation](#installation)
2. [Usage](#usage)
3. [License](#license)
4. [Contributions](#contributions)


# Inspiration

### Firstly, What is a Lambda Layer?

    A Lambda Layer is an archive containing [...] code.
    When you include a layer in an [AWS Lambda] function,
    the contents are extracted to [...] the execution environment.

As defined by [an AWS Compute blog.](https://aws.amazon.com/blogs/compute/using-lambda-layers-to-simplify-your-development-process/#:~:text=A%20Lambda%20layer%20is%20an,directory%20in%20the%20execution%20environment.)

### Ok, then what does this `layerd` library do?

Several steps of Layer inspection are automated here.

Currently, a Layer is deployed to AWS under 1) a Name and 2) a Version. Once a version is deployed (possibly by a Third-Party), how can you then see the contents of that layer?

One way would be to fumble around with the contents of the `/opt` directory in a lambda function. The equivalent to trying to lick your elbow.

Another way, only possible if created by a First-Party, would be to head to AWS, login, navigate to Lambda's page, 
enter the Layer subsection, choose a version, and press Download. From there, head to your local system, and unzip the contents. Of course the preferred way, 
but is greatly limited to solely First-Parties and takes several minutes of navigation and login to a 2FA system.

`layerd` automates the latter. `layerd` pings AWS Lambda, with the exact ARN of the Layer Version wanted, downloads, unzips, and mounts the contents locally. Within seconds. 

Not a bad way to save a few minutes.


# Installation

    $ pip3 install layerd


# Usage


#### CLI

The `layerd` script is automatically added to your OS's Path.
Call it with an ARN of a public lambda layer to mount the layer.

    $ layerd <ARN>

Example:

    $ layerd arn:aws:lambda:us-east-1:ACC:layer:LAYER-NAME:221

    Layer:    LAYER-NAME
    Region:   us-east-1
    V:        221

    Created: ./LAYER-NAME-221/

And pulled, unzipped, and mounted is the contents of the Lambda Layer.

    $ tree
    .
    └── LAYER-NAME-221/
        └── ...


#### Python Inline

The `layerd` module has a `layerd(arn: str)` function to mount a Lambda Layer.


    >>> from layerd import layerd

    >>> layerd('arn:aws:lambda:us-east-1:ACC:layer:LAYER-NAME:335')
    Layer:    LAYER-NAME
    Region:   us-east-1
    V:        335

    Created: ./LAYER-NAME-335/


Boom. You've mounted the Layer locally.

# License

`layerd` is licensed under the MIT License. See [LICENSE](LICENSE) for more.

# Contributions

Pull Requests for modifications are always welcome. Forks are preferred over Branches.

Want to become a maintainer? Submit 5 PRs, then we'll talk. 