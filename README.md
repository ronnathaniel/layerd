#  layerd

Mount and Inspect Lambda Layers in seconds.

> Lambda Layers created by a third party?
>
> Want the contents locally?
>
> Use `layerd`.


# Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [License](#license)
4. [Contributions](#contributions)

    

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